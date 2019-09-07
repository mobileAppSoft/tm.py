import os
import git
import json
from ui import create_list
from const import NOT_JSON, PATH
from formatters import formatTSP


def set_project(name=''):
    config = parse_config()
    projects = config['projects']
    if not len(projects):
        return False
    project_names = list(map(lambda x: x['name'], projects))
    # CLI component to set project interactive
    answer = create_list(
        'project', 'Set up the project you want to work on:', project_names)
    cur_project = ([
        x for x in projects if x['name'] == (name or answer['project'])])[0]
    config['cur_project'] = cur_project
    with open(PATH, 'w') as out_f:
        json.dump(config, out_f)
    return True


def set_params(params={}):
    config = parse_config()
    projects = config['projects']
    if not len(projects):
        return False
    cur_project = config['cur_project']
    cur_project = {**cur_project, **params}
    config['cur_project'] = cur_project
    with open(PATH, 'w') as out_f:
        json.dump(config, out_f)
    return True


def parse_config():
    with open(PATH, 'r') as f:
        data = f.read()
    try:
        return json.loads(data)
    except:
        raise Exception(PATH + NOT_JSON)


def get_project():
    config = parse_config()
    return config['cur_project']


def get_tm_project_repo():
    config = parse_config()
    project = config['cur_project']
    if(not project):
        return config['projects'][0]['tm_repo']
    else:
        return project['tm_repo']


def get_project_list():
    config = parse_config()
    print(list(map(lambda x: x['name'], config['projects'])))


def get_log_struct(title, desc):
    # TODO: handle initialize of git repo from tm.config.json
    project = get_project()
    repo = git.Repo(project['repo'])
    log = repo.refs[0].log()
    d = {
        '.Title': title,
        '.CreatedDate': formatTSP(False),
        '.Commit': log[0][1],
        '.Author': log[0].actor.name + ' <' + log[0].actor.email + '>',
        '.Date': formatTSP(log[0][3][0]),
        '.Desc': desc,
    }
    return d
