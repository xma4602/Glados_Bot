import datetime
import os
import re

from src.bot.Task import Task


def message(mes):
    mes = mes.split('\n')
    for i in range(len(mes)):
        mes[i] = mes[i].strip(' ')
        mes[i] = " ".join(mes[i].split())

    if mes[0] == '#задача':
        return task(mes[1:])

    return None


def task(task_data):
    # task_data = [title, manager, performers, deadline, description]
    task_data[1] = users_id([task_data[1]])[0]
    task_data[2] = users_id(task_data[2].replace(',', '').split())
    task_data[3] = time(task_data[3])
    task_data[4] = task_data[4:]
    return Task(task_data[0:5])


def time(dates=''):
    date = re.search(r'(\d{1,2})\.(\d{1,2})(.(\d{2,4}))?', dates)
    dates = dates.replace(date[0], '')
    time = re.search(r'(\d{1,2})([: ](\d{1,2}))?', dates)

    year = date.group(4)
    if year is None:
        year = datetime.datetime.today().year
    else:
        if len(year) == 4:
            year = int(year)
        else:
            year = int(year) + 2000

    minute = int(time.group(2)) if len(time.groups()) == 2 else 0

    return datetime.datetime(
        year=year,
        month=int(date.group(2)),
        day=int(date.group(1)),
        hour=int(time.group(1)),
        minute=minute
    )


def users_id(users_names):
    return [users.get(name.lower()) for name in users_names]


def club_users():
    os.chdir('..')
    file = open(r'src/club_council.txt', 'r', encoding="utf-8")
    try:
        data = file.readlines()
    finally:
        file.close()

    return dict((name.strip(), int(id.strip()))
                for name, id in (element.strip('\n').split(' ')
                                 for element in data))


users = club_users()
