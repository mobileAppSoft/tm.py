import os
import git
import json
from const import NOT_JSON
from formatters import formatTSP


def set_project(name=''):
    path = 'config/tm.config.json'
    with open(path, 'r') as f:
        data = f.read()
    try:
        config = json.loads(data)
        projects = config['projects']
        if not len(projects):
            return False
        cur_project = ([
            x for x in projects if x['name'] == name] or projects)[0]
        os.putenv('TM_CUR_PROJECT', cur_project['name'])
        os.putenv('TM_CUR_REPO', cur_project['repo'])
        return True
    except:
        raise Exception(path + NOT_JSON)


def get_project():
    get_env_var('TM_CUR_PROJECT')


def get_env_var(name):
    os.system('echo $' + name)


def get_repo():
    get_env_var('TM_CUR_REPO')


def get_project_list():
    path = 'config/tm.config.json'
    with open(path, 'r') as f:
        data = f.read()
    try:
        config = json.loads(data)
    except:
        raise Exception(path + NOT_JSON)
    print(config['projects'])


def get_log_struct(title):
    # TODO: handle initialize of git repo from tm.config.json
    repo = git.Repo(get_repo())
    log = repo.refs[0].log()
    d = {
        '.Title': title,
        '.CreatedDate': formatTSP(False),
        '.Commit': log[0][1],
        '.Author': log[0].actor.name + ' <' + log[0].actor.email + '>',
        '.Date': formatTSP(log[0][3][0]),
    }
    return d
