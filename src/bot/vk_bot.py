import asyncio
import datetime
import re

import aiohttp
import vk_api
from bs4 import BeautifulSoup
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.upload import VkUpload
from vk_api.utils import get_random_id

vk_session = vk_api.VkApi(
    token='vk1.a.fW6xhIXyLDwog_FX1fRTMiyEoVZL_b0ENm2J4y5lBKZ0hefDhJylNknLzd4I72GJ6'
          '--1rNhspg41efbhbJYPX1osNLmRCi9QBKo5v2AhBszehAZKPFUCby-7EeOkHOXXl_2Cp6Z8-0Hqo3yU9FF-B5811qznwiJq'
          '-uFEq_rOmUXkHde-9RvMTvm_T4WyFFNWsCd1baqaZA1mwaB69y9TSg')

longpoll = VkBotLongPoll(vk_session, '218320118')
vk = vk_session.get_api()
upload = VkUpload(vk)
a = 0
counter = 0
now = datetime.datetime.now()
date_remainder = now
time_remainder = now
default_datetime_remainder = now.replace(hour=0, minute=0, second=0, microsecond=0, day=1, month=1, year=1950)


def send(message, id):
    vk.messages.send(
        key='f25124946931a230031d57ddd73e4e0efcec4b7b',  # ВСТАВИТЬ ПАРАМЕТРЫ
        server='https://lp.vk.com/wh218320118',
        ts='42',
        random_id=get_random_id(),
        message=message,
        chat_id=id
    )


def hello(event):
    if event.from_chat:
        send('Привет!', event.chat_id)


def thanks(event):
    if event.from_chat:
        print(event.chat_id)
        send('Нет проблем! Рад стараться!', event.chat_id)


def anecdote(event):
    global counter
    if event.from_chat:
        async with aiohttp.ClientSession() as session:
            url = 'https://anekdotov.net/students/'
            response = await session.get(url)
            ans = await response.text()
        soup = BeautifulSoup(ans, 'html.parser')
        quotes = soup.find_all('div', class_='anekdot')
        print(quotes[counter].text)
        send_message = quotes[counter].text
        counter += 1
        print("counter: ", counter)
        send(send_message, event.chat_id)


def notice(event, message):
    # джарвиз, создай напоминание 06-02-2023 15:17 текст напоминания
    global date_remainder, time_remainder, default_datetime_remainder
    if event.from_chat:
        message = message.replace("jarvis, create a remider", "")
        message = message.replace("jarvis create a remider", "")
        message = message.replace("джарвиз, создай напоминание", "")
        message = message.replace("джарвиз создай напоминание", "")
        message = message.strip()
        for i in message:
            if i != " ":
                if i == "/" or i == "." or i == "\\" or i == ":":
                    i = "-"
                date_remainder += i
            while i != " ":
                time_remainder += i
        date_and_time = date_remainder.__str__() + " " + time_remainder.__str__()
        now_obj = datetime.datetime.strptime(date_and_time, '%d-%m-%Y %H:%M')
        if now_obj > default_datetime_remainder:
            default_datetime_remainder = now_obj


def unclear(event):
    if event.from_chat:
        send('Я не понимаю', event.chat_id)


def schedule(event):
    weekday = datetime.datetime.today().weekday()
    week = datetime.datetime.today().isocalendar()[1] - 5
    print(week)
    url = "https://ssau.ru/rasp?groupId=530994164&selectedWeek=" + str(week) + "&selectedWeekday=1"
    if event.from_chat:
        async with aiohttp.ClientSession() as session:
            response = await session.get(url)
            ans = await response.text()
        soup = BeautifulSoup(ans, 'html.parser')
        a = soup.find_all('div', class_='schedule__item')
        b = soup.find_all('div', class_='schedule__time-item')
        timetable = []
        clock = []
        for i in b:
            clock.append(i.text)
        print(clock)
        for i in a:
            timetable.append(i.text)
        print(timetable)
        str_timetable = ""
        if weekday == 0:
            weekday = timetable[1]
            str_timetable = clock[0] + " - " + clock[1] + '\n' + timetable[7] + '\n\n' + clock[2] + " - " + \
                            clock[3] + '\n' + timetable[13] + '\n\n' + clock[4] + " - " + clock[5] + '\n' + \
                            timetable[19] + '\n\n' + clock[6] + " - " + clock[7] + '\n' + timetable[
                                25] + '\n\n'
            print(str_timetable)
        if weekday == 1:
            weekday = timetable[2]
            str_timetable = clock[0] + " - " + clock[1] + '\n' + timetable[8] + '\n\n' + clock[2] + " - " + \
                            clock[3] + '\n' + timetable[14] + '\n\n' + clock[4] + " - " + clock[5] + '\n' + \
                            timetable[20] + '\n\n' + clock[6] + " - " + clock[7] + '\n' + timetable[
                                26] + '\n\n'
            print(str_timetable)
        if weekday == 2:
            weekday = timetable[3]
            str_timetable = clock[0] + " - " + clock[1] + '\n' + timetable[9] + '\n\n' + clock[2] + " - " + \
                            clock[3] + '\n' + timetable[15] + '\n\n' + clock[4] + " - " + clock[5] + '\n' + \
                            timetable[21] + '\n\n' + clock[6] + " - " + clock[7] + '\n' + timetable[
                                27] + '\n\n'
            print(str_timetable)
        if weekday == 3:
            weekday = timetable[4]
            str_timetable = clock[0] + " - " + clock[1] + '\n' + timetable[10] + '\n\n' + clock[2] + " - " + \
                            clock[3] + '\n' + timetable[16] + '\n\n' + clock[4] + " - " + clock[5] + '\n' + \
                            timetable[22] + '\n\n' + clock[6] + " - " + clock[7] + '\n' + timetable[
                                28] + '\n\n'
            print(str_timetable)
        if weekday == 4:
            weekday = timetable[5]
            str_timetable = clock[0] + " - " + clock[1] + '\n' + timetable[11] + '\n\n' + clock[2] + " - " + \
                            clock[3] + '\n' + timetable[17] + '\n\n' + clock[4] + " - " + clock[5] + '\n' + \
                            timetable[23] + '\n\n' + clock[6] + " - " + clock[7] + '\n' + timetable[
                                29] + '\n\n'
            print(str_timetable)
        if weekday == 5:
            weekday = timetable[6]
            str_timetable = clock[0] + " - " + clock[1] + '\n' + timetable[12] + '\n\n' + clock[2] + " - " + \
                            clock[3] + '\n' + timetable[18] + '\n\n' + clock[4] + " - " + clock[5] + '\n' + \
                            timetable[24] + '\n\n' + clock[6] + " - " + clock[7] + '\n' + timetable[
                                30] + '\n\n'
            print(str_timetable)
        if weekday == 6:
            weekday = "Воскресенье"
            str_timetable = "Сегодня пар нет)))\nМожно отдыхать\n"
        send(f"Сегодня {weekday}", event.chat_id)
        send(str_timetable, event.chat_id)


async def bot(event):
    global date_remainder
    global time_remainder
    global counter
    if event.type == VkBotEventType.MESSAGE_NEW:
        message = event.object.message.get('text').lower()
        a = list(event.object.values())[0].get('from_id')
        print(a)
        if re.match('jarvis ', message) or re.match('джарвиз ', message) \
                or re.match('jarvis, ', message) or re.match('джарвиз, ', message) \
                or re.match('jarvis', message) or re.match('джарвиз', message):
            if re.search('привет', message) or re.search('hi', message):
                hello(event)
            elif re.search('спасибо', message):
                thanks(event)
            elif re.search('дай анекдот', message):
                anecdote(event)
            elif re.search('создай напоминание', message) or re.search('create a reminder', message):
                notice(event, message)
            elif re.search('расписание', message) or re.search('timetable', message):
                schedule(event)
            else:
                unclear(event)


async def main():
    for event in longpoll.listen():
        try:
            await bot(event)
        except vk_api.exceptions.ApiError:
            continue


if __name__ == '__main__':
    asyncio.run(main())
