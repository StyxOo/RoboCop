import os
import json


_config_path = './config.json'


def _create_config():
    data = {'ip': '192.0.0.1', 'port': '1880', 'url': '/fail', 'save': False}

    with open(_config_path, 'w') as conf_file:
        json.dump(data, conf_file)


#  Check if config exists and create default if not
if not os.path.isfile(_config_path):
    print("No configuration file found. Creating default configuration file")
    _create_config()

with open(_config_path) as config_file:
    _config = json.load(config_file)
