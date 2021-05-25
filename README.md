# Chatbot Example

![demo](assets/demo.gif)
# Backend

## Installation

Python 3.8.10 is needed. Tested on Windows 10 64bit.
```
pip install -r requirements.txt
python -m spacy download en_core_web_md
python -m spacy download de_core_news_sm
```

## Train

```
cd backend

doit train
doit train_de
```

## Run interactive
```
cd backend
doit run_core
doit run_core_de
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

## Date extraction

see https://rasa.com/docs/rasa/components#ducklingentityextractor

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
