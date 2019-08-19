import inquirer


def create_list(name, question, options):
    questions = [
        inquirer.List(name,
                      message=question,
                      choices=options,
                      ),
    ]
    return inquirer.prompt(questions)
