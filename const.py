TASK_TMP = '''###### {{.CreatedDate}}

# {{.Title}}

---

```
commit {{.Commit}}
Author: {{.Author}}
Date:   {{.Date}}


```
'''
CLIENT = '.client'
PROJECT = '.project'
TASK = '.task'

MODE = '0700'


# Exceptions

NOT_JSON = ' not a valid JSON file!'
