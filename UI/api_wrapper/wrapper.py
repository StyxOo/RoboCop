import os
import json
import requests
from . import _config


def _create_request_url():
    url = 'http'
    if _config['save']:
        url += 's'
    url += '://{}:{}/move'.format(_config['ip'], _config['port'])
    return url


def _send_request(f1=None, f2=None, f3=None, f4=None, f5=None):
    payload = {}
    if f1 is not None:
        payload['finger1'] = f1
    if f2 is not None:
        payload['finger2'] = f2
    if f3 is not None:
        payload['finger3'] = f3
    if f4 is not None:
        payload['finger4'] = f4
    if f5 is not None:
        payload['finger5'] = f5
    r = requests.get(_create_request_url(), params=payload)
    print("Request returned status: {}".format(r.status_code))


def _clamp_percent(value):
    if value < 0:
        print("Less than 0 percent specified for extension. Clamping to 0")
        value = 0
    elif value > 100:
        print("More than 100 percent specified for extension. Clamping to 100")
        value = 100
    return value


def move_finger1(percent):
    percent = _clamp_percent(percent)
    _send_request(f1=percent)


def move_finger2(percent):
    percent = _clamp_percent(percent)
    _send_request(f2=percent)


def move_finger3(percent):
    percent = _clamp_percent(percent)
    _send_request(f3=percent)


def move_finger4(percent):
    percent = _clamp_percent(percent)
    _send_request(f4=percent)


def move_finger5(percent):
    percent = _clamp_percent(percent)
    _send_request(f5=percent)


def move_hand(f1, f2, f3, f4, f5):
    f1 = _clamp_percent(f1)
    f2 = _clamp_percent(f2)
    f3 = _clamp_percent(f3)
    f4 = _clamp_percent(f4)
    f5 = _clamp_percent(f5)
    _send_request(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5)


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
