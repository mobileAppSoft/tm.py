import requests
import json
import time
from repo import parse_config
from fs import create_task
from jira import JIRA
from ui import create_list, progress, spinner


def get_creds():
    config = parse_config()
    try:
        creds = config['cur_project']['boards']['jira']
        return creds['server'], creds['username'], creds['password']
    except ValueError:
        print('tm.config.json does not have trello info')


def authorize():
    server, username, token = get_creds()
    return JIRA({'server': server}, basic_auth=(username, token))


def get_my_projects(jira):
    if not jira:
        jira = authorize()
        return jira.projects()
    else:
        return jira.projects()


def get_my_issues():
    spin = spinner()
    for _ in range(5):
        time.sleep(0.1)
        spin.next()
    jira = authorize()
    projects = get_my_projects(jira)
    project_names = list(map(lambda x: x.name, projects))
    answer = create_list('project', 'Select project', project_names)
    project = ([
        x for x in projects if x.name == answer['project']])[0]
    return jira.search_issues('project=' + project.key +
                              ' and assignee = currentUser() and status not in (resolved, done) order by priority desc')


def _import():
    pass


#jira = JIRA('https://jira.atlassian.com')
