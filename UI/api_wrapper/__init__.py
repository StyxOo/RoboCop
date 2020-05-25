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


def _write_config():
    if os.path.isfile(_config_path):
        os.remove(_config_path)

    with open(_config_path, 'w') as config_file:
        json.dump(_config, config_file)


def set_ip(ip, store=False):
    _config['ip'] = ip
    if store:
        _write_config()


def set_port(port, store=False):
    _config['port'] = port
    if store:
        _write_config()


def set_url(url, store=False):
    _config['url'] = url
    if store:
        _write_config()


def set_use_save_connection(use_save_connection, store=False):
    _config['save'] = use_save_connection
    if store:
        _write_config()