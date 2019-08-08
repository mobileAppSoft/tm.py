import os
import click
import re
import const
from fs import isTask


def process_tmp(tmp, tmp_map):
    for key in tmp_map:
        tmp = re.sub('{{'+key+'}}', tmp_map[key], tmp)
    return tmp


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
    os.makedirs(project_path, const.MODE)
    os.open(os.path.join(project_path, const.PROJECT),
            os.O_RDONLY | os.O_CREAT, const.MODE)
    print("initialize has been done successfully")


cli.add_command(init)


if __name__ == '__main__':
    cli()
