import os
import re
from repo import get_log_struct
from const import CLIENT, PROJECT, TASK, MODE, TASK_TMP


def process_tmp(tmp, tmp_map):
    for key in tmp_map:
        tmp = re.sub('{{'+key+'}}', tmp_map[key], tmp)
    return tmp


def createClient(title):
    pass


def createProject(title, path=os.getcwd()):
    os.makedirs(path, MODE)
    os.makedirs(path + '/Backlog', MODE)
    os.makedirs(path + '/Progress', MODE)
    os.makedirs(path + '/Done', MODE)
    os.makedirs(path + '/TechDebt', MODE)
    os.open(os.path.join(path, PROJECT),
            os.O_RDONLY | os.O_CREAT, MODE)


def createTask(title):
    cwd = os.getcwd()
    print(cwd)
    os.makedirs(title, MODE)
    os.makedirs(os.path.join(cwd+'/'+title, 'Extras'), MODE)
    os.open(os.path.join(cwd+'/'+title, TASK),
            os.O_RDONLY | os.O_CREAT)
    f = open(os.path.join(cwd+'/'+title, title + '.md'), 'w+')
    f.write(process_tmp(TASK_TMP, get_log_struct(title)))
    f.close()


def isClient():
    return os.path.isfile(CLIENT)


def isProject():
    return os.path.isfile(PROJECT)


def isTask():
    return os.path.isfile(TASK)
