import contextlib
import itertools
import json
import logging
import os
from typing import Iterator, Optional, Text, Iterable, Union, Dict, Callable
from time import sleep

from rasa.core.tracker_store import SQLTrackerStore, TrackerStore
from rasa.core.domain import Domain
from rasa.core.brokers.event_channel import EventChannel
from rasa.core.trackers import DialogueStateTracker


logger = logging.getLogger(__name__)

class OracleTrackerStore(SQLTrackerStore):
    """Store which can save and retrieve trackers from an Oracle database."""

    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

    class OracleEvent(Base):
        """Represents an event in the Oracle Tracker Store"""

        from sqlalchemy import Column, Integer, String, Float, Text, Sequence

        __tablename__ = "events"

        id = Column(Integer, Sequence('id_seq'), primary_key=True)
        sender_id = Column(String(255), nullable=False, index=True)
        type_name = Column(String(255), nullable=False)
        timestamp = Column(Float)
        intent_name = Column(String(255))
        action_name = Column(String(255))
        value = Column(Text)
        text = Column(Text)
        data = Column(Text)

    def __init__(
        self,
        domain: Optional[Domain] = None,
        dialect: Text = "oracle",
        host: Optional[Text] = None,
        port: Optional[int] = None,
        url: Optional[Text] = None,
        db: Text = "rasa.db",
        username: Text = None,
        password: Text = None,
        event_broker: Optional[EventChannel] = None,
        query: Optional[Dict] = None,
    ) -> None:
        from sqlalchemy.orm import sessionmaker
        from sqlalchemy import create_engine
        import sqlalchemy.exc

        engine_url = SQLTrackerStore.get_db_url(
            dialect, host, port, db, username, password, None, query
        )
        logger.debug(
            "Attempting to connect to database via '{}'.".format(repr(engine_url))
        )

        # Database might take a while to come up
        while True:
            try:
                # pool_size and max_overflow can be set to control the number of
                # connections that are kept in the connection pool. Not available
                # for SQLite, and only  tested for postgresql. See
                # https://docs.sqlalchemy.org/en/13/core/pooling.html#sqlalchemy.pool.QueuePool
                self.engine = create_engine(engine_url, max_identifier_length=30)

                try:
                    self.Base.metadata.create_all(self.engine)
                except (
                    sqlalchemy.exc.OperationalError,
                    sqlalchemy.exc.ProgrammingError,
                ) as e:
                    # Several Rasa services started in parallel may attempt to
                    # create tables at the same time. That is okay so long as
                    # the first services finishes the table creation.
                    logger.error(f"Could not create tables: {e}")

                self.sessionmaker = sessionmaker(bind=self.engine)
                break
            except (
                sqlalchemy.exc.OperationalError,
                sqlalchemy.exc.IntegrityError,
            ) as error:

                logger.warning(error)
                sleep(5)

        logger.debug(f"Connection to SQL database '{db}' successful.")
        # pylint: disable=bad-super-call
        super(SQLTrackerStore, self).__init__(domain, event_broker)

    def save(self, tracker: DialogueStateTracker) -> None:
        """Update database with events from the current conversation."""

        if self.event_broker:
            self.stream_events(tracker)

        with self.session_scope() as session:
            # only store recent events
            events = self._additional_events(session, tracker)

            for event in events:
                data = event.as_dict()

                intent = data.get("parse_data", {}).get("intent", {}).get("name")
                action = data.get("name")
                timestamp = data.get("timestamp")
                text = data.get("text")
                value = data.get("value")

                # noinspection PyArgumentList
                session.add(
                    self.OracleEvent(
                        sender_id=tracker.sender_id,
                        type_name=event.type_name,
                        timestamp=timestamp,
                        intent_name=intent,
                        action_name=action,
                        text=text,
                        value=value,
                        data=json.dumps(data, ensure_ascii=True),
                    )
                )
            session.commit()

        logger.debug(
            "Tracker with sender_id '{}' "
            "stored to database".format(tracker.sender_id)
        )
