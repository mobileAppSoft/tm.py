import os
import json
import sys
import shutil
import re
from repo import get_log_struct, get_project, get_tm_project_repo
from const import CLIENT, PROJECT, TASK, MODE, TASK_TMP, bcolors


def process_tmp(tmp, tmp_map):
    for key in tmp_map:
        tmp = re.sub('{{'+key+'}}', tmp_map[key], tmp)
    return tmp


def create_client(title):
    pass


def fs_to_JSON(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [fs_to_JSON(os.path.join(path, x)) for x in os.listdir
                         (path)]
    else:
        d['type'] = "file"
    return d


def create_project(title, path=os.getcwd()):
    os.makedirs(path, MODE)
    os.makedirs(path + '/Backlog', MODE)
    os.makedirs(path + '/Progress', MODE)
    os.makedirs(path + '/Done', MODE)
    os.makedirs(path + '/TechDebt', MODE)
    os.open(os.path.join(path, PROJECT),
            os.O_RDONLY | os.O_CREAT, MODE)


def create_task(title, status='Progress', desc=''):
    cwd = get_tm_project_repo()
    task_dir = str(cwd + '/' + status + '/' + title)
    if os.path.isdir(task_dir):
        print(bcolors.ERROR +
              "Error: Task already exists" + bcolors.ENDC)
        sys.exit()
    os.mkdir(task_dir, MODE)
    os.mkdir(os.path.join(task_dir, 'Extras'), MODE)
    os.open(os.path.join(task_dir, TASK),
            os.O_RDONLY | os.O_CREAT)
    f = open(os.path.join(task_dir, title + '.md'), 'w+')
    f.write(process_tmp(TASK_TMP, get_log_struct(title, desc)))
    f.close()


def is_client():
    return os.path.isfile(CLIENT)


def is_project():
    return os.path.isfile(PROJECT)


def is_task():
    return os.path.isfile(TASK)


def move_task(task, folder='Done'):
    root = get_tm_project_repo()
    shutil.move(os.path.join(root + '/Progress/', task), root + '/' + folder)
