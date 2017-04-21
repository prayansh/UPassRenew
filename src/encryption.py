import base64
import getpass
import json
import os

import keyring

SERVICE_NAME = 'UPass'
config_file = 'config.dat'
_here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(_here, config_file)


def login_credentials():
    if os.path.isfile(filename):
        user = get_user()
        password = get_pass(user)
    else:
        user, password = keyring_auth()
    return user, password


def keyring_auth():
    username = raw_input("Please enter your username: ")
    keyring.set_password(SERVICE_NAME, username, base64.b64encode(getpass.getpass()))
    # output username to file
    with open(filename, 'w') as f:
        data = {'username': username}
        json.dump(data, f)
    return username, get_pass(username)


def get_pass(username):
    return base64.b64decode(keyring.get_password(SERVICE_NAME, username))


def get_user():
    with open(filename, 'r') as f:
        data = json.load(f)
        return data['username']
