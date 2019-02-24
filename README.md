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
doit train
doit train_core

doit train_de
doit train_core_de
```

## Run interactive
```
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

# Frontend

Run the following command in the frontend folder
```
livereload
```
