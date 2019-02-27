# Chatbot Example

![demo](assets/demo.gif)
# Backend

## Installation

Python 3.6.8 is needed. Tested on Windows 10 64bit.
```
pip install -r requirements.txt
python -m spacy download en_core_web_md
python -m spacy download de
```

## Train

```
cd backend

doit train
doit train_core

doit train_de
doit train_core_de
```

## Run interactive
```
cd backend
doit run_core
```

## Run Socket.io server
```
doit core_server
doit core_server_de
```

## Run action server
```
doit run_actions
```

## Deploy container in openshift

```
oc process -f deploy-openshift.yml | oc create -f -
oc start-build chatbot-core --from-dir . --follow
```

## Connect to mongodb instance to check tracking
```
oc get pods
# find pod for mongodb and open terminal:
oc rsh chatbot-mongodb-1-23hsj
$ mongo 127.0.0.1:27017/$MONGODB_DATABASE -u $MONGODB_USER -p $MONGODB_PASSWORD
$ use sampledb
$ db.conversations.find()
```

## Delete everything from OpenShift
```
oc delete all -l app=chatbot
oc delete all -l app=chatbot-mongodb
oc delete secret chatbot-mongodb
oc delete all -l build=chatbot-core
oc delete dc,route -l app=chatbot-core
```

# Frontend

Run the following command in the frontend folder
```
cd frontend
livereload
```
