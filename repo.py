import git
from formatters import formatTSP

# TODO: handle initialize of git repo from tm.config
repo = git.Repo('.')


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
