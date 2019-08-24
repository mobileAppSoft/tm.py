TASK_TMP = '''###### {{.CreatedDate}}

# {{.Title}}

---

```
commit {{.Commit}}
Author: {{.Author}}
Date:   {{.Date}}

```
{{.Desc}}
'''
CLIENT = '.client'
PROJECT = '.project'
TASK = '.task'

MODE = 0o755

# Configuration

PATH = 'config/tm.config.json'

# Exceptions

NOT_JSON = ' not a valid JSON file!'


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[31m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
