import requests
import json
from repo import parse_config


def get_users_issues(parameter_list):
    config = parse_config()
    return config['cur_project']['boards']['trello']


def get_boards():
    config = parse_config()
    key = config['cur_project']['boards']['trello']['key']
    token = config['cur_project']['boards']['trello']['token']
    url = 'https://api.trello.com/1/boards/5bab58ffb5f96804c74f737e/cards?key={0}&token={1}'.format(
        key, token)
    res = json.loads(requests.get(
        url).text)
    return res
