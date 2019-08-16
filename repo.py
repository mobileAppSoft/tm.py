import git
import json
from const import NOT_JSON
from formatters import formatTSP


path = 'config/tm.config.json'
with open(path, 'r') as f:
    data = f.read()
try:
    config = json.loads(data)
except:
    raise Exception(path + NOT_JSON)

# TODO: handle initialize of git repo from tm.config
repo = git.Repo('.')


def getJSON():
    print(config['repo'])


def getLogStruct(title):
    log = repo.refs[0].log()
    d = {
        '.Title': title,
        '.CreatedDate': formatTSP(False),
        '.Commit': log[0][1],
        '.Author': log[0].actor.name + ' <' + log[0].actor.email + '>',
        '.Date': formatTSP(log[0][3][0]),
    }
    return d
