import os
import shutil
import re
from repo import get_log_struct
from const import CLIENT, PROJECT, TASK, MODE, TASK_TMP


def process_tmp(tmp, tmp_map):
    for key in tmp_map:
        tmp = re.sub('{{'+key+'}}', tmp_map[key], tmp)
    return tmp


def create_client(title):
    pass


def create_project(title, path=os.getcwd()):
    os.makedirs(path, MODE)
    os.makedirs(path + '/Backlog', MODE)
    os.makedirs(path + '/Progress', MODE)
    os.makedirs(path + '/Done', MODE)
    os.makedirs(path + '/TechDebt', MODE)
    os.open(os.path.join(path, PROJECT),
            os.O_RDONLY | os.O_CREAT, MODE)


def create_task(title):
    cwd = os.getcwd()
    print(cwd)
    os.makedirs(title, MODE)
    os.makedirs(os.path.join(cwd+'/'+title, 'Extras'), MODE)
    os.open(os.path.join(cwd+'/'+title, TASK),
            os.O_RDONLY | os.O_CREAT)
    f = open(os.path.join(cwd+'/'+title, title + '.md'), 'w+')
    f.write(process_tmp(TASK_TMP, get_log_struct(title)))
    f.close()


def is_client():
    return os.path.isfile(CLIENT)


def is_project():
    return os.path.isfile(PROJECT)


def is_task():
    return os.path.isfile(TASK)


def move_task(task, folder):
    pass
