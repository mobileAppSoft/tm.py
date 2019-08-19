import os
import click
import re
import const
import git
import formatters
from repo import set_project, get_project
from fs import is_project, is_client, create_task, create_client, create_project


@click.group()
def cli():
    pass


@click.command()
@click.argument('client')
@click.argument('project')
def init(client, project):
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

    os.makedirs(client, const.MODE)
    client_path = os.path.join(cwd, client)
    os.open(client_path + '/' + const.CLIENT,
            os.O_RDONLY | os.O_CREAT, const.MODE)
    project_path = os.path.join(client_path, project)
    create_project(project, project_path)
    print("initialize has been done successfully")


@click.command()
@click.option('--title', help='Title of entity')
def add(title):
    create_project(title) if is_client() else create_task(title)


cli.add_command(init)
cli.add_command(add)

if __name__ == '__main__':
    сli()
