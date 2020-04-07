import os
import click
import re
import const
import json
import formatters
from jira_api import _import as jira_import
from ui import create_list
from repo import set_project, get_project, add_project
from fs import is_project, is_client, create_task, create_client, create_project, move_task, fs_to_JSON


@click.group()
def cli():
    pass


@click.command()
@click.option("-client", help="Name of the client")
@click.option("-project", help="Title of the project")
def init(client, project):
    if client and project:
        cwd = os.getcwd()

        # +-----+---+--------------------------+
        # | rwx | 7 | Read, write and execute |
        # | rw - | 6 | Read, write |
        # | r-x | 5 | Read, and execute |
        # | r-- | 4 | Read,                    |
        # | -wx | 3 | Write and execute |
        # | -w - | 2 | Write |
        # | --x | 1 | Execute |
        # | --- | 0 | no permissions |
        # +------------------------------------+

        # +------------+------+-------+
        # | Permission | Octal | Field |
        # +------------+------+-------+
        # | rwx------ | 0700 | User |
        # | ---rwx--- | 0070 | Group |
        # | ------rwx | 0007 | Other |
        # +------------+------+-------+
        client_path = os.path.join(cwd, client)
        os.mkdir(client_path, const.MODE)
        os.open(client_path + '/' + const.CLIENT,
                os.O_RDONLY | os.O_CREAT, const.MODE)
        project_path = os.path.join(client_path, project)
        create_project(project, project_path)
        print("initialize has been done successfully")
    else:
        print("Please, specify the client and the project")


@click.command()
@click.option('-task', help='Task name')
@click.option('-status', help='Move task to another status')
def mv(task, status):
    move_task(task)


@click.command()
@click.option('-path', help='Path to the tm project folder')
def openf(path):
    if path:
        add_project(path)
    else:
        print("Please, specify path of the project")


@click.command()
@click.option('--title', help='Title of entity')
@click.option('--status', help='Create task in status')
def add(title, status):
    create_project(title) if is_client() else create_task(title, status)


@click.command()
def setpr():
    set_project()


@click.command()
def fetch():
    answer = create_list('its', 'Select ITS', ['Trello', 'JIRA'])
    if answer['its'] == 'JIRA':
        jira_import()


cli.add_command(init)
cli.add_command(add)
cli.add_command(mv)
cli.add_command(fetch)
cli.add_command(openf)
cli.add_command(setpr)

if __name__ == '__main__':
    cli()
