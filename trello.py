import requests
import json
import time
from repo import parse_config
from fs import create_task
from ui import create_list, progress, spinner

host = 'https://api.trello.com/1'


def get_creds():
    config = parse_config()
    try:
        creds = config['cur_project']['boards']['trello']
        return creds['key'], creds['token']
    except ValueError:
        print('tm.config.json does not have trello info')


def get_me():
    key, token = get_creds()
    url = host + '/members/me?key={0}&token={1}'.format(
        key, token)
    me = json.loads(requests.get(
        url).text)
    return me


def get_boards(member_id=None):
    key, token = get_creds()
    # to avoid redundant call
    if not member_id:
        me = get_me()
        user_id = me['id']
    else:
        user_id = member_id
    me = get_me()
    user_id = me['id']
    url = host + '/members/'+user_id+'/boards?key={0}&token={1}'.format(
        key, token)
    boards = json.loads(requests.get(
        url).text)
    return boards


def get_cards(member_id=None):
    spin = spinner()
    for _ in range(5):
        time.sleep(0.1)
        spin.next()

    key, token = get_creds()
    if not member_id:
        me = get_me()
        user_id = me['id']
    else:
        user_id = member_id

    boards = get_boards(user_id)
    board_names = list(map(lambda x: x['name'], boards))
    answer = create_list('board', 'Select board', board_names)
    board = ([
        x for x in boards if x['name'] == answer['board']])[0]
    url = host + '/boards/'+board['id']+'/cards?key={0}&token={1}'.format(
        key, token)
    res = json.loads(requests.get(
        url).text)
    return res


def get_my_issues():
    me = get_me()
    user_id = me['id']
    cards = get_cards(user_id)
    my_issues = [x for x in cards if user_id in x['idMembers']]
    return list(map(lambda x: [x['id'], x['name'], x['desc'], x['due']], my_issues))


def get_my_boards(member_id=None):
    if not member_id:
        me = get_me()
        user_id = me['id']
    else:
        user_id = member_id
    boards = get_boards(user_id)
    return boards


def _import():
    issues = get_my_issues()
    _len = len(issues)
    bar = progress('Trello issues import: ', _len)
    for i in range(_len):
        create_task(issues[i][1], desc=issues[i][2])
        bar.next()
    bar.finish()


# def _import():
#     issues = get_my_issues()
#     _len = len(issues)
#     bar = progress('Trello issues import: ', _len)
#     for i in range(_len):
#         create_task(issues[i][1], desc=issues[i][2])
#         bar.next()
#     bar.finish()
