#!/bin/bash

if [ ! -z "$USE_MONGO_TRACKER" ]; then
echo "Adding tracker store to endpoints.";
cat <<'EOF' >> endpoints.yml

tracker_store:
  store_type: mongod
  url: mongodb://${MONGODB_HOST}
  db: ${MONGODB_DBNAME}
  username: ${MONGODB_USER}
  password: ${MONGODB_PASS}
  auth_source: ${MONGODB_DBNAME}
EOF
else
echo "No tracker store";
fi
cat endpoints.yml
