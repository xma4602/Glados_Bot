import datetime
import os
import re

from src.bot.Task import Task


# главный метод парсинга сообщения
def message(text: str, sender_id: str):
    """
    Получает и текст сообщения и обрабатывает его.
    Не возвращает результат.
    :param text: string текст соотщения
    """

    # разбиваем на строки и очищаем от пробелов
    text = text.split('\n')
    for i in range(len(text)):
        text[i] = text[i].strip(' ')
        text[i] = " ".join(text[i].split())

    # если в заголовке тег задачи, отправляем на парсинг задачи
    if text[0] == '#задача':
        return task(text[1:], sender_id)


def task(task_data: list, sender_id: str):
    """
    Получает и парсит данные о задаче
    :param task_data: массив данных задачи.
    task_data = [заголовок, организатор, список исполнителей, дедлайн, описание]
    :return: экземпляр Task
    """

    # вызываем методы парсинга для каждого поля
    task_data[1] = users_id(task_data[1].replace(',', '').split())
    task_data[2] = time(task_data[2])
    task_data[3] = task_data[3:]

    task_data = dict(
        title=task_data[0],
        manager_id=sender_id,
        performers_id=task_data[1],
        deadline=task_data[2],
        description=task_data[3]
    )

    return Task(task_data)


def time(date_time):
    """
    Получает и парсит данные о времени
    :param date_time: дата и время
    :return: экземпляр datetime
    """
    # регуляркой находим дату
    date = re.search(r'(\d{1,2})\.(\d{1,2})(.(\d{2,4}))?', date_time)
    # удаляем дату из текста
    date_time = date_time.replace(date[0], '')
    # регуляркой находим времяя
    time = re.search(r'(\d{1,2})([: ](\d{1,2}))?', date_time)

    # проверяем наличие года и дообрабатываем его
    year = date.group(4)
    if year is None:
        year = datetime.datetime.today().year
    else:
        if len(year) == 4:
            year = int(year)
        else:
            year = int(year) + 2000

    # проверяем наличие минут и дообрабатываем их
    minute = int(time.group(2)) if len(time.groups()) == 2 else 0

    # возвращаем экземпляр даты-времени
    return datetime.datetime(
        year=year,
        month=int(date.group(2)),
        day=int(date.group(1)),
        hour=int(time.group(1)),
        minute=minute
    )


def users_id(users_surnames):
    """
    Получиет имена пользователей и возвращает их id
    :param users_surnames: список фамилий пользователей
    :return: список соответствующих фамилиям id
    """
    # по ключам фамилий из словаря users формируем список id
    return [users.get(surname.lower()) for surname in users_surnames]


def club_users():
    """
    Считывает с файла записи о фамилия-id и заносит в словарь.
    :return: словарь фамилия-id членов совета клуба
    """
    os.chdir('..')
    # считываем записи построчно
    with open(r'src/club_council.txt', 'r', encoding="utf-8") as file:
        data = file.readlines()

    # каждую строку забиваем на слова и парсим в фамилия-id
    return dict((surname, int(id))
                for surname, id in (surname_id.strip('\n').split(' ')
                                    for surname_id in data))


"""
Операция создания словаря фамилия-id членов совета клуба
!НЕ УДАЛЯТЬ!
"""
users = club_users()
