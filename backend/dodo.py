from doit.tools import Interactive
def task_train():
    """Train nlu"""
    return {
        "actions": [
            'python -m rasa_nlu.train -c nlu_config.yml --data data/train.md -o models --fixed_model_name nlu --project current --verbose'
        ],
        'file_dep': ["nlu_config.yml", "data/train.md"],
        'targets': ["models/current/nlu/crf_model.pkl", "models/current/nlu/intent_classifier_sklearn.pkl"],
    }

def task_train_de():
    """Train nlu DE"""
    return {
        "actions": [
            'python -m rasa_nlu.train -c nlu_config_de.yml --data data/train_de.md -o models_de --fixed_model_name nlu --project current --verbose'
        ],
        'file_dep': ["nlu_config.yml", "data/train_de.md"],
        'targets': ["models_de/current/nlu/crf_model.pkl", "models_de/current/nlu/intent_classifier_sklearn.pkl"],
    }

def task_run_nlu():
    """ Run rasa server """
    return {
        "actions": [
            Interactive('python -m rasa_nlu.server --path ./models')
        ],
        'file_dep': ["models/current/nlu/crf_model.pkl", "models/current/nlu/intent_classifier_sklearn.pkl"],
        "uptodate": [False],
    }

def task_run_nlu_de():
    """ Run rasa server DE """
    return {
        "actions": [
            Interactive('python -m rasa_nlu.server --path ./models_de')
        ],
        'file_dep': ["models_de/current/nlu/crf_model.pkl", "models_de/current/nlu/intent_classifier_sklearn.pkl"],
        "uptodate": [False],
    }

def task_train_core():
    """ Train rasa core """
    return {
        "actions": [
            'python -m rasa_core.train -d domain.yml -s data/stories.md -o models/current/dialogue -c policies.yml'
        ],
        'file_dep': ["domain.yml", "data/stories.md", "policies.yml",
            "models/current/nlu/crf_model.pkl", "models/current/nlu/intent_classifier_sklearn.pkl",
        ],
        'targets': ["models/current/dialogue/domain.json"],
    }

def task_train_core_de():
    """ Train rasa core DE """
    return {
        "actions": [
            'python -m rasa_core.train -d domain_de.yml -s data/stories.md -o models_de/current/dialogue -c policies.yml'
        ],
        'file_dep': ["domain_de.yml", "data/stories.md", "policies.yml",
        ],
        'targets': ["models_de/current/dialogue/domain.json"],
    }

def task_run_actions():
    """ Run rasa action server """
    return {
        "actions": [Interactive('python -m rasa_core_sdk.endpoint -p 5055 --actions actions')],
        'file_dep': ["actions.py"],
        "uptodate": [False],
    }

def task_run_core():
    """ Run rasa server """
    return {
        "actions": [Interactive('python -m rasa_core.run -d models/current/dialogue -u models/current/nlu')],
        'file_dep': ["models/current/dialogue/domain.json"],
        "uptodate": [False],
    }

def task_run_core_de():
    """ Run rasa server """
    return {
        "actions": [Interactive('python -m rasa_core.run -d models_de/current/dialogue -u models_de/current/nlu --endpoints endpoints.yml')],
        'file_dep': ["models_de/current/dialogue/domain.json"],
        "uptodate": [False],
    }

def task_core_server():
    """ Run rasa server """
    return {
        "actions": [Interactive('python -m rasa_core.run -d models/current/dialogue -u models/current/nlu --port 5005 --cors "*" --credentials credentials.yml  --endpoints endpoints.yml')],
        'file_dep': ["models/current/dialogue/domain.json", "credentials.yml", "endpoints.yml",
            "models/current/nlu/crf_model.pkl", "models/current/nlu/intent_classifier_sklearn.pkl"],
        "uptodate": [False],
    }

def task_core_server_de():
    """ Run rasa server """
    return {
        "actions": [Interactive('python -m rasa_core.run -d models_de/current/dialogue -u models_de/current/nlu --port 5005 --cors "*" --credentials credentials.yml  --endpoints endpoints.yml')],
        'file_dep': ["models_de/current/dialogue/domain.json", "credentials.yml", "endpoints.yml",
            "models_de/current/nlu/crf_model.pkl", "models_de/current/nlu/intent_classifier_sklearn.pkl"],
        "uptodate": [False],
    }
