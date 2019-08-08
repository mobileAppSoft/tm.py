import os
from const import CLIENT, PROJECT, TASK


def createClient(parameter_list):
    pass


def createProject(parameter_list):
    pass


def createTask(parameter_list):
    pass


def isClient(parameter_list):
    return os.path.isfile(CLIENT)


def isProject(parameter_list):
    return os.path.isfile(PROJECT)


def isTask():
    return os.path.isfile(TASK)
