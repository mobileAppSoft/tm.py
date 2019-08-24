import time
import inquirer
from progress.bar import Bar
from progress.spinner import PixelSpinner


def create_list(name, question, options):
    questions = [
        inquirer.List(name,
                      message=question,
                      choices=options,
                      ),
    ]
    return inquirer.prompt(questions)


def progress(title='Processing', _max=20):
        # for i in range(20):
        #         time.sleep(1)
        #         bar.next()
        #     bar.finish()
    return Bar(title, max=_max)


def spinner():
    spinner = PixelSpinner()
    return spinner
