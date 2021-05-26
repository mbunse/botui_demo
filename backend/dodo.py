from doit.tools import Interactive
def task_train_nlu():
    """Train nlu"""
    return {
        "actions": [
            'rasa train nlu --nlu data/nlu.yml --config config.yml --domain domain.yml --out models --fixed-model-name nlu -v '
        ],
        'file_dep': ["config.yml", "data/nlu.yml", "domain.yml"],
        'targets': ["models/nlu.tar.gz"],
    }
def task_train_core():
    """Train nlu"""
    return {
        "actions": [
            'rasa train core --stories data --config config.yml --domain domain.yml --out models --fixed-model-name core -v '
        ],
        'file_dep': ["config.yml", "data/stories.yml", "data/rules.yml", "domain.yml"],
        'targets': ["models/core.tar.gz"],
    }

def task_train():
    """Train nlu"""
    return {
        "actions": [
            'rasa train --data data --config config.yml --domain domain.yml --out models --fixed-model-name model -v '
        ],
        'file_dep': ["config.yml", "data/nlu.yml", "data/stories.yml", "data/rules.yml", "domain.yml"],
        'targets': ["models/model.tar.gz"],
    }
def task_train_de():
    """Train nlu DE"""
    return {
        "actions": [
            'rasa train --data data_de/ --config config_de.yml --domain domain_de.yml --out models_de --fixed-model-name model -v '
        ],
        'file_dep': ["config_de.yml", "data_de/nlu.yml", "data_de/stories.yml", "data_de/rules.yml", "domain_de.yml"],
        'targets': ["models_de/model.tar.gz"],
    }

def task_run_actions():
    """ Run rasa action server """
    return {
        "actions": [Interactive('rasa run actions -p 5055 -vv')],
        'file_dep': ["actions.py"],
        "uptodate": [False],
    }

def task_shell():
    """ Run rasa server """
    return {
        "actions": [Interactive('rasa shell -m models/model.tar.gz --endpoints endpoints.yml')],
        'file_dep': ["models/model.tar.gz", "endpoints.yml"],
        "uptodate": [False],
    }

def task_shell_de():
    """ Run rasa server """
    return {
        "actions": [Interactive('rasa shell -m models_de/model.tar.gz --endpoints endpoints.yml')],
        'file_dep': ["models_de/model.tar.gz", "endpoints.yml"],
        "uptodate": [False],
    }

def task_interactive():
    """ Run rasa server """
    return {
        "actions": [Interactive('rasa interactive -m models/model.tar.gz --endpoints endpoints.yml --config config.yml --domain domain.yml --data data/')],
        'file_dep': ["models/model.tar.gz", "endpoints.yml", "config.yml", "data/nlu.yml", "data/stories.yml", "domain.yml"],
        "uptodate": [False],
    }

def task_interactive_de():
    """ Run rasa server """
    return {
        "actions": [Interactive('rasa interactive -m models_de/model.tar.gz --endpoints endpoints.yml --config config_de.yml --domain domain_de.yml --data data_de/')],
        'file_dep': ["models_de/model.tar.gz", "endpoints.yml", "config_de.yml", "data_de/nlu.yml", "data_de/stories.yml", "domain_de.yml"],
        "uptodate": [False],
    }

def task_core_server():
    """ Run rasa server """
    return {
        "actions": [Interactive('rasa run -m models/model.tar.gz --port 5005 --cors "*" --credentials credentials.yml --endpoints endpoints.yml -vv')],
        'file_dep': ["models/model.tar.gz", "credentials.yml", "endpoints.yml"],
        "uptodate": [False],
    }

def task_core_server_de():
    """ Run rasa server """
    return {
        "actions": [Interactive('rasa run -m models_de/model.tar.gz --port 5005 --cors "*" --credentials credentials.yml --endpoints endpoints.yml')],
        'file_dep': ["models_de/model.tar.gz", "credentials.yml", "endpoints.yml"],
        "uptodate": [False],
    }
