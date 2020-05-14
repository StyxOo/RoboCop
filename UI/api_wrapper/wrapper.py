"""
This is the main module of the api_wrapper package. It is responsible for creating and sending HTTP requests to the
robotic hands controller.
"""

import os
import json
import requests
from . import _config
from . import _config_path


# Saves current configuration to config file
def _write_config():
    if os.path.isfile(_config_path):
        os.remove(_config_path)

    with open(_config_path, 'w') as config_file:
        json.dump(_config)


# Set the ip of the current configuration. If it should be saved in the config.json, pass store=True
def set_ip(ip, store=False):
    _config['ip'] = ip
    if store:
        _write_config()


# Set the port of the current configuration. If it should be saved in the config.json, pass store=True
def set_port(port, store=False):
    _config['port'] = port
    if store:
        _write_config()


# Set the url of the current configuration. If it should be saved in the config.json, pass store=True
def set_url(url, store=False):
    _config['url'] = url
    if store:
        _write_config()


# Should http or https be used for the connection? If it should be saved in the config.json, pass store=True
def set_use_save_connection(use_save_connection, store=False):
    _config['save'] = use_save_connection
    if store:
        _write_config()


# Internal function which create the requests url from the current configuration.
def _create_request_url():
    url = 'http'
    if _config['save']:
        url += 's'
    url = '{}:{}{}'.format(_config['ip'], _config['port'], _config['url'])
    print(url)
    return url


# Sends a HTTP request. Creates query parameters from given finger inputs.
def _send_request(f1=None, f2=None, f3=None, f4=None, f5=None):
    payload = {}
    if f1 is not None:
        payload['f1'] = f1
    if f2 is not None:
        payload['f2'] = f2
    if f3 is not None:
        payload['f3'] = f3
    if f4 is not None:
        payload['f4'] = f4
    if f5 is not None:
        payload['f5'] = f5
    print(payload)
    r = requests.get(_create_request_url(), params=payload)
    print("Request returned status: {}".format(r.status_code))


# Clamps a percent value between 0 and 100. Is used to make sure query parameters do not extend percent values.
def _clamp_percent(value):
    if value < 0:
        print("Less than 0 percent specified for extension. Clamping to 0")
        value = 0
    elif value > 100:
        print("More than 100 percent specified for extension. Clamping to 100")
        value = 100
    return value


# Call this function with a percent value between 0 and 100 to move only the first finger
def move_finger1(percent):
    percent = _clamp_percent(percent)
    _send_request(f1=percent)


# Call this function with a percent value between 0 and 100 to move only the second finger
def move_finger2(percent):
    percent = _clamp_percent(percent)
    _send_request(f2=percent)


# Call this function with a percent value between 0 and 100 to move only the third finger
def move_finger3(percent):
    percent = _clamp_percent(percent)
    _send_request(f3=percent)


# Call this function with a percent value between 0 and 100 to move only the fourth finger
def move_finger4(percent):
    percent = _clamp_percent(percent)
    _send_request(f4=percent)


# Call this function with a percent value between 0 and 100 to move only the fifth finger
def move_finger5(percent):
    percent = _clamp_percent(percent)
    _send_request(f5=percent)


# Call this with percents between 0 and 100 for each finger. Makes the whole hand move.
def move_hand(f1, f2, f3, f4, f5):
    f1 = _clamp_percent(f1)
    f2 = _clamp_percent(f2)
    f3 = _clamp_percent(f3)
    f4 = _clamp_percent(f4)
    f5 = _clamp_percent(f5)
    _send_request(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5)


# This function can make the whole hand move. Parameters are optional, so the fingers to move can be chosen.
def move_fingers(f1=None, f2=None, f3=None, f4=None, f5=None):
    if f1 is not None:
        f1 = _clamp_percent(f1)
    if f2 is not None:
        f2 = _clamp_percent(f2)
    if f3 is not None:
        f3 = _clamp_percent(f3)
    if f4 is not None:
        f4 = _clamp_percent(f4)
    if f5 is not None:
        f5 = _clamp_percent(f5)
    _send_request(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5)
