from src.bot.Task import Task

task_title = '#задача'


def parse_message(message):
    message = message.split('\n')
    for i in range(len(message)):
        message[i] = message[i].strip(' ')
        message[i] = " ".join(message[i].split())

    if message[0] == task_title:
        return parse_task(message[1:])

    return None


def parse_task(task_data):
    # info = [title, manager, performers, deadline, description]
    task_data[2] = task_data[2].replace(',', '').split()
    task_data[3] = task_data[3].split()
    return Task(task_data)
