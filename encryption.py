import base64
import getpass
import json
import os

import keyring

SERVICE_NAME = 'UPass'
config_file = 'config.dat'
_here = os.path.dirname(os.path.abspath(__file__))


def login_credentials():
    filename = os.path.join(_here, config_file)
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
    with open(config_file, 'wa') as f:
        data = {'username': username}
        json.dump(data, f)
    f.close()
    return username, get_pass(username)


def get_pass(username):
    return base64.b64decode(keyring.get_password(SERVICE_NAME, username))


def get_user():
    filename = os.path.join(_here, config_file)
    with open(filename, 'r') as f:
        data = json.load(f)
        return data['username']
