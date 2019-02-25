#!/bin/bash

if [ -z "$MONGODB_HOST" ]; then
cat <<EOF >> environment.yml
tracker_store:
    store_type: mongod
    url: mongodb://@$MONGODB_HOST>
    db: $MONGODB_DBNAME
    username: $MONGODB_USER
    password: $MONGODB_PASS
EOF
fi
