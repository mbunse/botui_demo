from doit.tools import Interactive
def task_train():
    """Train nlu"""
    return {
        "actions": [
            'rasa train --data nlu_data/ --config nlu_config.yml --domain domain.yml --out models --fixed-model-name nlu -v '
        ],
        'file_dep': ["nlu_config.yml", "nlu_data/nlu.yml", "nlu_data/stories.yml", "domain.yml"],
        'targets': ["models/nlu.tar.gz"],
    }

def task_train_de():
    """Train nlu DE"""
    return {
        "actions": [
            'rasa train --data nlu_data_de/ --config nlu_config_de.yml --domain domain_de.yml --out models_de --fixed-model-name nlu -v '
        ],
        'file_dep': ["nlu_config_de.yml", "nlu_data_de/nlu.yml", "nlu_data_de/stories.yml", "domain_de.yml"],
        'targets': ["models_de/nlu.tar.gz"],
    }

def task_run_actions():
    """ Run rasa action server """
    return {
        "actions": [Interactive('rasa run actions -p 5055')],
        'file_dep': ["actions.py"],
        "uptodate": [False],
    }

def task_run_core():
    """ Run rasa server """
    return {
        "actions": [Interactive('rasa shell -m models/nlu.tar.gz --endpoints endpoints.yml')],
        'file_dep': ["models/nlu.tar.gz", "endpoints.yml"],
        "uptodate": [False],
    }

def task_run_core_de():
    """ Run rasa server """
    return {
        "actions": [Interactive('rasa shell -m models_de/nlu.tar.gz --endpoints endpoints.yml')],
        'file_dep': ["models_de/nlu.tar.gz", "endpoints.yml"],
        "uptodate": [False],
    }

def task_interactive():
    """ Run rasa server """
    return {
        "actions": [Interactive('rasa interactive -m models/nlu.tar.gz --endpoints endpoints.yml --config nlu_config.yml --domain domain.yml --data nlu_data/')],
        'file_dep': ["models/nlu.tar.gz", "endpoints.yml", "nlu_config.yml", "nlu_data/nlu.yml", "nlu_data/stories.yml", "domain.yml"],
        "uptodate": [False],
    }

def task_interactive_de():
    """ Run rasa server """
    return {
        "actions": [Interactive('rasa interactive -m models_de/nlu.tar.gz --endpoints endpoints.yml --config nlu_config_de.yml --domain domain_de.yml --data nlu_data_de/')],
        'file_dep': ["models_de/nlu.tar.gz", "endpoints.yml", "nlu_config_de.yml", "nlu_data_de/nlu.yml", "nlu_data_de/stories.yml", "domain_de.yml"],
        "uptodate": [False],
    }

def task_core_server():
    """ Run rasa server """
    return {
        "actions": [Interactive('rasa run -m models/nlu.tar.gz --port 5005 --cors "*" --credentials credentials.yml --endpoints endpoints.yml')],
        'file_dep': ["models/nlu.tar.gz", "credentials.yml", "endpoints.yml"],
        "uptodate": [False],
    }

def task_core_server_de():
    """ Run rasa server """
    return {
        "actions": [Interactive('rasa run -m models_de/nlu.tar.gz --port 5005 --cors "*" --credentials credentials.yml --endpoints endpoints.yml')],
        'file_dep': ["models_de/nlu.tar.gz", "credentials.yml", "endpoints.yml"],
        "uptodate": [False],
    }
