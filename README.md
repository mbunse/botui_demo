# Chatbot Example

![demo](assets/demo.gif)
# Backend

## Installation

Python 3.6.8 is needed. Tested on Windows 10 64bit.
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

## Create db

Get oracle xe (Express edition)
Run [`prepare_db.sql`](prepare_db.sql) to create user.
Install oracle instantclient Basic (Light) (see https://oracle.github.io/odpi/doc/installation.html#linux): 


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

## Debug settings for vscode

```{json}
{
    "name": "Rase: core de",
    "type": "python",
    "request": "launch",
    "program": "path/to/bin/rasa",
    "env": {
        "FLASK_APP": "app.py",
        "FLASK_ENV": "development",
        "FLASK_DEBUG": "0"
    },
    "cwd": "${workspaceFolder}/backend",
    "args": [
        "run",
        "--model",
        "models/nlu.tar.gz",
        "--port",
        "5005",
        "--cors",
        "'*'",
        "--credentials",
        "credentials.yml",
        "--endpoints",
        "endpoints.yml"
    ],
    "justMyCode": false
}
```