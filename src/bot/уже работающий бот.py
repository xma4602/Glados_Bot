import vk_api, vk
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import requests
import urllib3
vk_session = vk_api.VkApi(token='vk1.a.fW6xhIXyLDwog_FX1fRTMiyEoVZL_b0ENm2J4y5lBKZ0hefDhJylNknLzd4I72GJ6--1rNhspg41efbhbJYPX1osNLmRCi9QBKo5v2AhBszehAZKPFUCby-7EeOkHOXXl_2Cp6Z8-0Hqo3yU9FF-B5811qznwiJq-uFEq_rOmUXkHde-9RvMTvm_T4WyFFNWsCd1baqaZA1mwaB69y9TSg')
longpoll = VkBotLongPoll(vk_session, '218320118')
vk = vk_session.get_api()
import asyncio
import aiohttp
import re
import aiosqlite as sql
from bs4 import BeautifulSoup
import datetime
import socket
a=0
counter=0
def send(message, id):
    vk.messages.send(
        key=('f25124946931a230031d57ddd73e4e0efcec4b7b'),  # ВСТАВИТЬ ПАРАМЕТРЫ
        server=('https://lp.vk.com/wh218320118'),
        ts=('42'),
        random_id=get_random_id(),
        message=message,
        chat_id=id,
    )
async def bot(event):
    try:
        if event.type == VkEventType.USER_TYPING_IN_CHAT:
            print('Печатает ', event.user_id, 'в беседе', event.chat_id)



        if event.type == VkBotEventType.MESSAGE_NEW:#Если пришло новое сообщение

            print("Откуда: ", event.object.peer_id)
            print("От кого: ", event.object.from_id)
            print(event.object)

            message=event.object.message.get('text').lower()
            person=list(event.object.values())[0].get('from_id')#определяет id написавшего
            if person==100822494:
                person="Олеган"
            elif person==210242776:
                person="Колян"

            #работает на методе поиска ключевых слов в строке с помощью бибилиотеки re

            if re.match('jarvis', message) or re.match('джарвиз',message) or re.match('jarvis,',message) or re.match('джарвиз,',message) or re.match('бот', message) or re.match('bot', message):
                if re.match('джарвиз',message) or re.match('jarvis,',message):
                    message=message[7:]
                elif re.match('jarvis', message):
                    message=message[6:]
                elif re.match('джарвиз,',message):
                    message=message[8:]
                elif re.match('бот', message) or re.match('bot', message):
                    message=message[3:]
                message=message.strip()
                if re.search('привет', message) or re.search('hi', message):
                    if event.from_group:
                        print("++++++++++++++++++++++")
                        print(event.group_id)
                    if event.from_user:
                        print("!!!!!!!!!!!!!!!!!")
                        print(event.type)
                    if event.from_chat:
                        if person=="Колян":
                            send('Здорово, Колян', event.chat_id)
                            vk.messages.send(peer_id=210242776, message='Здорово, Колян', random_id=0)
                        if person == "Олеган":
                            send("Здорово, Олеган", event.chat_id)
                elif re.search('спасибо', message):
                    if event.from_chat:
                        send('Нет проблем!Рад стараться!', event.chat_id)

                #добавление и удаление информации с базы данных(здесь можно будет таким принципом записывать что угодно)

                elif re.search("купить", message):
                    message=message[6:]
                    message = message.strip()
                    message=message.split("\n")
                    message = list(set(message))
                    for i in message:
                        async with sql.connect("buy.db") as db:
                            await db.execute("INSERT INTO buy VALUES (?,?)", (i,person,))
                            await db.commit()
                    send("Записал", event.chat_id)
                elif re.search("список", message):
                    async with sql.connect("buy.db") as db:
                        bd = await db.execute("SELECT * FROM buy")
                        bd = await bd.fetchall()
                    kol=""
                    olg=""
                    if bd==[]:
                        send("Список пуст", event.chat_id)
                    else:
                        for i in bd:
                            if i[1]=="Колян":
                                kol+=(i[0]+"\n")
                            if i[1]=="Олеган":
                                olg += (i[0] + "\n")
                        st="Колян просил купить: \n"+kol+"\nОлеган просил купить: \n" + olg
                        send(st, event.chat_id)
                elif re.search("все купил", message) or re.search("купил все", message):
                    async with sql.connect("buy.db") as db:
                        await db.execute("DELETE FROM buy;")
                        await db.commit()
                    send("Ок. Я подкорректировал список", event.chat_id)
                elif re.search("купил", message):
                    message = message[5:]
                    message = message.strip()
                    message=message.split("\n")
                    async with sql.connect("buy.db") as db:
                        bd = await db.execute("SELECT * FROM buy")
                        bd = await bd.fetchall()
                        for i in message:
                            await db.execute("DELETE FROM buy WHERE something = ?",(i,))
                            await db.commit()
                    send("Ок. Я подкорректировал список", event.chat_id)

                #получение расписания занятий в универе
                #расписание берется с сайта университета

                elif re.search('расписание', message) or re.search('timetable', message):
                    message = message.strip()
                    message = message.replace("расписание", "")
                    message = message.replace("timetable", "")
                    message = message.strip()
                    message=message.replace("\\","/")
                    message=message.replace(".","/")
                    message=message.replace(" ","/")
                    print(message)
                    # можно получить расписание на вчера, завтра и послезавтра
                    if message != '':
                        if message=="завтра":
                            weekday = datetime.datetime.today()
                            weekday = weekday.replace(day=datetime.datetime.today().day + 1)
                            week = weekday.isocalendar()[1] - 5
                            print(week)
                            weekday=weekday.weekday()
                            print(weekday)
                        elif message=="послезавра":
                            weekday = datetime.datetime.today()
                            weekday = weekday.replace(day=datetime.datetime.today().day + 2)
                            week = weekday.isocalendar()[1] - 5
                            print(week)
                            weekday=weekday.weekday()
                            print(weekday)
                        elif message=="вчера":
                            weekday = datetime.datetime.today()
                            weekday = weekday.replace(day=datetime.datetime.today().day -1)
                            week = weekday.isocalendar()[1] - 5
                            print(week)
                            weekday=weekday.weekday()
                            print(weekday)
                        #либо на любой календарный день
                        else:
                            weekday = datetime.datetime.strptime(message, "%d/%m")
                            print(weekday)
                            week=weekday.isocalendar()[1]-5
                            weekday=weekday.weekday()-1
                    else:
                        weekday = datetime.datetime.today().weekday()
                        week = datetime.datetime.today().isocalendar()[1] - 5
                    if person=="Колян":
                        url = "https://ssau.ru/rasp?groupId=530994164&selectedWeek=" + str(week) + "&selectedWeekday=1"
                    if person=="Олеган":
                        url = "https://ssau.ru/rasp?groupId=530996168$selectedWeek=" + str(week) + "&selectedWeekday=1"
                    print(url)

                    #парсинг

                    if event.from_chat:
                        async with aiohttp.ClientSession() as session:
                            response = await session.get(url)
                            ans = await response.text()
                        soup = BeautifulSoup(ans, 'html.parser')
                        a = soup.find_all('div', class_='schedule__item')
                        b = soup.find_all('div', class_='schedule__time-item')
                        print(b)
                        if b!=[]:
                            timetable = []
                            clock = []
                            for i in b:
                                clock.append(i.text)
                            for i in a:
                                timetable.append(i.text)
                            str_timetable = ""
                            print(weekday)
                            if weekday == 0:
                                weekday = timetable[1]
                                str_timetable = clock[0] + " - " + clock[1] + '\n' + timetable[7] + '\n\n' + clock[2] + " - " + \
                                                clock[3] + '\n' + timetable[13] + '\n\n' + clock[4] + " - " + clock[5] + '\n' + \
                                                timetable[19] + '\n\n' + clock[6] + " - " + clock[7] + '\n' + timetable[
                                                    25] + '\n\n'
                            if weekday == 1:
                                weekday = timetable[2]
                                str_timetable = clock[0] + " - " + clock[1] + '\n' + timetable[8] + '\n\n' + clock[2] + " - " + \
                                                clock[3] + '\n' + timetable[14] + '\n\n' + clock[4] + " - " + clock[5] + '\n' + \
                                                timetable[20] + '\n\n' + clock[6] + " - " + clock[7] + '\n' + timetable[
                                                    26] + '\n\n'
                            if weekday == 2:
                                weekday = timetable[3]
                                str_timetable = clock[0] + " - " + clock[1] + '\n' + timetable[9] + '\n\n' + clock[2] + " - " + \
                                                clock[3] + '\n' + timetable[15] + '\n\n' + clock[4] + " - " + clock[5] + '\n' + \
                                                timetable[21] + '\n\n' + clock[6] + " - " + clock[7] + '\n' + timetable[
                                                    27] + '\n\n'
                            if weekday == 3:
                                weekday = timetable[4]
                                str_timetable = clock[0] + " - " + clock[1] + '\n' + timetable[10] + '\n\n' + clock[2] + " - " + \
                                                clock[3] + '\n' + timetable[16] + '\n\n' + clock[4] + " - " + clock[5] + '\n' + \
                                                timetable[22] + '\n\n' + clock[6] + " - " + clock[7] + '\n' + timetable[
                                                    28] + '\n\n'
                            if weekday == 4:
                                weekday = timetable[5]
                                str_timetable = clock[0] + " - " + clock[1] + '\n' + timetable[11] + '\n\n' + clock[2] + " - " + \
                                                clock[3] + '\n' + timetable[17] + '\n\n' + clock[4] + " - " + clock[5] + '\n' + \
                                                timetable[23] + '\n\n' + clock[6] + " - " + clock[7] + '\n' + timetable[
                                                    29] + '\n\n'
                            if weekday == 5:
                                weekday = timetable[6]
                                str_timetable = clock[0] + " - " + clock[1] + '\n' + timetable[12] + '\n\n' + clock[2] + " - " + \
                                                clock[3] + '\n' + timetable[18] + '\n\n' + clock[4] + " - " + clock[5] + '\n' + \
                                                timetable[24] + '\n\n' + clock[6] + " - " + clock[7] + '\n' + timetable[
                                                    30] + '\n\n'
                            if weekday == 6:
                                weekday = "Воскресенье"
                                str_timetable = "Отдыхай))\nПар нет😄"
                            if str_timetable==-1:
                                str_timetable="На это время не существует расписания"
                            print(str_timetable)
                        else:
                            weekday="На эту дату расписания не существует"
                            str_timetable="Ничего не могу с этим сделать(((\nОбратитесь к программисьам сайта Самарского университета"
                        send(f"{weekday}", event.chat_id)
                        send(str_timetable, event.chat_id)

                #недописанная функция дедлайнов

                elif re.search("дедлайн", message) or re.search("дэдлайн", message):
                    message = message[7:]
                    message=message.lstrip('\n')
                    message=message.split('\n')
                    try:
                        weekday = datetime.datetime.strptime(message[0], "%d/%m %H:%M")
                    except ValueError:
                        weekday = datetime.datetime.strptime(message[0], "%d/%m/%Y %H:%M")





                else:
                    if event.from_chat:
                        send('Я не понимаю', event.chat_id)
        await asyncio.sleep(1)
    except ValueError:
        send("Введите правильную дату", event.chat_id)
    except:
        send("Неизвестная ошибка\nОбратитесь к разработчику отправив сообщение в группе https://vk.com/public218320118")
async def main():
    async with sql.connect("buy.db") as db:
        await db.execute("CREATE TABLE IF NOT EXISTS 'buy' ('something' STRING, 'person' STRING)")
        await db.commit()
    while True:
        for event in longpoll.listen():#слушаем лонгпулл запросы
            try:
                await asyncio.wait([loop.create_task(bot(event))])
            except socket.timeout:
                continue
            except urllib3.exceptions.ReadTimeoutError:
                continue
            except vk_api.exceptions.ApiError:
                continue
            except requests.exceptions.ReadTimeout:
                continue
if __name__=='__main__':
    loop = asyncio.new_event_loop()#оборачиваем все в корутины для асинхронности
    asyncio.set_event_loop(loop)
    while True:
        try:
            loop.run_until_complete(main())
        except socket.timeout:
            continue
        except urllib3.exceptions.ReadTimeoutError:
            continue
        except vk_api.exceptions.ApiError:
            continue
        except requests.exceptions.ReadTimeout:
            continue