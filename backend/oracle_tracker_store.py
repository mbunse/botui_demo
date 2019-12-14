import contextlib
import itertools
import json
import logging
import os
from typing import Iterator, Optional, Text, Iterable, Union, Dict, Callable
from time import sleep

from rasa.core.tracker_store import TrackerStore
from rasa.core.domain import Domain
from rasa.core.brokers.event_channel import EventChannel
from rasa.core.trackers import DialogueStateTracker


logger = logging.getLogger(__name__)

class OracleTrackerStore(TrackerStore):
    """Store which can save and retrieve trackers from an SQL database."""

    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

    class SQLEvent(Base):
        """Represents an event in the SQL Tracker Store"""

        from sqlalchemy import Column, Integer, String, Float, Text, Sequence

        __tablename__ = "events"

        id = Column(Integer, Sequence('id_seq'), primary_key=True)
        sender_id = Column(String(255), nullable=False, index=True)
        type_name = Column(String(255), nullable=False)
        timestamp = Column(Float)
        intent_name = Column(String(255))
        action_name = Column(String(255))
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

        engine_url = self.get_db_url(
            dialect, host, port, db, username, password, query
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

        super().__init__(domain, event_broker)

    @staticmethod
    def get_db_url(
        dialect: Text = "sqlite",
        host: Optional[Text] = None,
        port: Optional[int] = None,
        db: Text = "rasa.db",
        username: Text = None,
        password: Text = None,
        query: Optional[Dict] = None,
    ) -> Union[Text, "URL"]:
        """Builds an SQLAlchemy `URL` object representing the parameters needed
        to connect to an SQL database.

        Args:
            dialect: SQL database type.
            host: Database network host.
            port: Database network port.
            db: Database name.
            username: User name to use when connecting to the database.
            password: Password for database user.
            query: Dictionary of options to be passed to the dialect and/or the
                DBAPI upon connect.

        Returns:
            URL ready to be used with an SQLAlchemy `Engine` object.

        """
        from urllib.parse import urlsplit
        from sqlalchemy.engine.url import URL

        # Users might specify a url in the host
        parsed = urlsplit(host or "")
        if parsed.scheme:
            return host

        if host:
            # add fake scheme to properly parse components
            parsed = urlsplit("schema://" + host)

            # users might include the port in the url
            port = parsed.port or port
            host = parsed.hostname or host

        return URL(
            dialect,
            username,
            password,
            host,
            port,
            database=db,
            query=query,
        )

    @contextlib.contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        session = self.sessionmaker()
        try:
            yield session
        finally:
            session.close()

    def keys(self) -> Iterable[Text]:
        """Returns sender_ids of the SQLTrackerStore"""
        with self.session_scope() as session:
            sender_ids = session.query(self.SQLEvent.sender_id).distinct().all()
            return [sender_id for (sender_id,) in sender_ids]

    def retrieve(self, sender_id: Text) -> Optional[DialogueStateTracker]:
        """Create a tracker from all previously stored events."""

        with self.session_scope() as session:
            query = session.query(self.SQLEvent)
            result = (
                query.filter_by(sender_id=sender_id)
                .order_by(self.SQLEvent.timestamp)
                .all()
            )

            events = [json.loads(event.data) for event in result]

            if self.domain and len(events) > 0:
                logger.debug(f"Recreating tracker from sender id '{sender_id}'")
                return DialogueStateTracker.from_dict(
                    sender_id, events, self.domain.slots
                )
            else:
                logger.debug(
                    "Can't retrieve tracker matching "
                    "sender id '{}' from SQL storage. "
                    "Returning `None` instead.".format(sender_id)
                )
                return None

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

                # noinspection PyArgumentList
                session.add(
                    self.SQLEvent(
                        sender_id=tracker.sender_id,
                        type_name=event.type_name,
                        timestamp=timestamp,
                        intent_name=intent,
                        action_name=action,
                        data=json.dumps(data),
                    )
                )
            session.commit()

        logger.debug(
            "Tracker with sender_id '{}' "
            "stored to database".format(tracker.sender_id)
        )

    def _additional_events(
        self, session: "Session", tracker: DialogueStateTracker
    ) -> Iterator:
        """Return events from the tracker which aren't currently stored."""

        n_events = (
            session.query(self.SQLEvent.sender_id)
            .filter_by(sender_id=tracker.sender_id)
            .count()
            or 0
        )

        return itertools.islice(tracker.events, n_events, len(tracker.events))
