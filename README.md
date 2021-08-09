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

Manual download of language packages:
```
curl -L --output de_core_news_md-3.0.0-py3-none-any.whl --url https://github.com/explosion/spacy-models/releases/download/de_core_news_md-3.0.0/de_core_news_md-3.0.0-py3-none-any.whl
curl -L --output en_core_web_md-3.0.0-py3-none-any.whl --url https://github.com/explosion/spacy-models/releases/download/en_core_web_md-3.0.0/en_core_web_md-3.0.0-py3-none-any.whl
pip install en_core_web_md-3.0.0-py3-none-any.whl
pip install de_core_news_md-3.0.0-py3-none-any.whl
```

# Backend

The backend is found in the `backend` folder.

## Train

Intent recognition and conversation flow prediction have to be trained
```
doit train
```

## Run interactive

First, start the action server: `doit run_action`. Then:
```
doit interactive
```

## Run Socket.io/REST server
```
doit run_actions
doit core_server
```

# Frontend

Run the following command in the frontend folder
```
cd frontend
livereload -p 8080
```

The socketio frontend is available as http://localhost:8080/index.html, the REST version as http://localhost:8080/index_rest.html.

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
