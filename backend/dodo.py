from doit.tools import Interactive
def task_train():
    """Train nlu"""
    return {
        "actions": [
            'python -m rasa_nlu.train -c nlu_config.yml --data data/train.md -o models --fixed_model_name nlu --project current --verbose'
        ]
    }

def task_run_nlu():
    """ Run rasa server """
    return {
        "actions": [
            Interactive('python -m rasa_nlu.server --path ./models')
        ]
    }

def task_train_core():
    """ Train rasa core """
    return {
        "actions": [
            'python -m rasa_core.train -d domain.yml -s data/stories.md -o models/current/dialogue -c policies.yml'
        ]
    }

def task_run_core():
    """ Run rasa server """
    return {
        "actions": [Interactive('python -m rasa_core.run -d models/current/dialogue -u models/current/nlu')]
    }

def task_core_server():
    """ Run rasa server """
    return {
        "actions": [Interactive('python -m rasa_core.run -d models/current/dialogue -u models/current/nlu --port 5005 --cors "*" --credentials credentials.yml')]
    }
    