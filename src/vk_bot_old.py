# import vk_api
# import requests
# from vk_api.longpoll import VkLongPoll, VkEventType
#
# session=requests.Session()
# login, password='89091205955','thjdvn628@$F$HhH'
# vk_session=vk_api.VkApi(login, password)
# try:
#     vk_session.auth(token_only=True)
# except vk_api.AuthError as error_msg:
#     print(error_msg)
#
# longpoll = VkLongPoll(vk_session)
# vk = vk_session.get_api()
# for event in longpoll.listen():
#     if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
#    #Слушаем longpoll, если пришло сообщение то:
#         if event.text == 'Первый вариант фразы' or event.text == 'Второй вариант фразы': #Если написали заданную фразу
#             if event.from_user: #Если написали в ЛС
#                 vk.messages.send( #Отправляем сообщение
#                     user_id=event.user_id,
#                     message='Ваш текст'
# 		)
#             elif event.from_chat: #Если написали в Беседе
#                 vk.messages.send( #Отправляем собщение
#                     chat_id=event.chat_id,
#                     message='Ваш текст'
# 		)

# import random, vk_api, vk
# from vk_api.keyboard import VkKeyboard, VkKeyboardColor
# from vk_api.utils import get_random_id
# vk_session = vk_api.VkApi(token='143')
# from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
# longpoll = VkBotLongPoll(vk_session, 143)
# vk = vk_session.get_api()
# from vk_api.longpoll import VkLongPoll, VkEventType
# Lslongpoll = VkLongPoll(vk_session)
# Lsvk = vk_session.get_api()
#
# keyboard = VkKeyboard(one_time=True)
# keyboard.add_button('Привет', color=VkKeyboardColor.NEGATIVE)
# keyboard.add_button('Клавиатура', color=VkKeyboardColor.POSITIVE)
# keyboard.add_line()
# keyboard.add_location_button()
# keyboard.add_line()
# keyboard.add_vkpay_button(hash="action=transfer-to-group&group_id=143")
#
# for event in longpoll.listen():
#     if event.type == VkBotEventType.MESSAGE_NEW:
#         if 'Ку' in str(event) or 'Привет' in str(event) or 'Хай' in str(event) or 'Хелло' in str(event) or 'Хеллоу' in str(event):
#             if event.from_chat:
#                 vk.messages.send(
#                     key = (''),          #ВСТАВИТЬ ПАРАМЕТРЫ
#                     server = (''),
#                     ts=(''),
#                     random_id = get_random_id(),
#               	    message='Привет!',
#             	    chat_id = event.chat_id
#                     )
#         if 'Клавиатура' in str(event):
#             if event.from_chat:
#                 vk.messages.send(
#                     keyboard = keyboard.get_keyboard(),
#                     key = (''),          #ВСТАВИТЬ ПАРАМЕТРЫ
#                     server = (''),
#                     ts=(''),
#                     random_id = get_random_id(),
#               	    message='Держи',
#              	    chat_id = event.chat_id
#             	    )
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from lxml import html

import vk_api, vk
from vk_api.upload import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

vk_session = vk_api.VkApi(token='vk1.a.fW6xhIXyLDwog_FX1fRTMiyEoVZL_b0ENm2J4y5lBKZ0hefDhJylNknLzd4I72GJ6--1rNhspg41efbhbJYPX1osNLmRCi9QBKo5v2AhBszehAZKPFUCby-7EeOkHOXXl_2Cp6Z8-0Hqo3yU9FF-B5811qznwiJq-uFEq_rOmUXkHde-9RvMTvm_T4WyFFNWsCd1baqaZA1mwaB69y9TSg')

longpoll = VkBotLongPoll(vk_session, '218320118')
vk = vk_session.get_api()
# Lslongpoll = VkLongPoll(vk_session)
# Lsvk = vk_session.get_api()


upload = VkUpload(vk)



import aiohttp
import asyncio
from aiohttp import web

import re
import datetime
#keyboard = VkKeyboard(one_time=True)
#keyboard.add_button('Привет', color=VkKeyboardColor.NEGATIVE)
#keyboard.add_button('Клавиатура', color=VkKeyboardColor.POSITIVE)
# keyboard.add_line()
# keyboard.add_location_button()
# keyboard.add_line()
#keyboard.add_vkpay_button(hash="action=transfer-to-group&group_id=218320118")
a=0
counter=0
def send(message, id):
    vk.messages.send(
        key=('f25124946931a230031d57ddd73e4e0efcec4b7b'),  # ВСТАВИТЬ ПАРАМЕТРЫ
        server=('https://lp.vk.com/wh218320118'),
        ts=('42'),
        random_id=get_random_id(),
        message=message,
        chat_id=id
    )

# def upload_photo(upload, photo):
#     response = upload.photo_messages(photo)[0]
#
#     owner_id = response['owner_id']
#     photo_id = response['id']
#     access_key = response['access_key']
#
#     return owner_id, photo_id, access_key
#
#
# def send_photo(vk, peer_id, owner_id, photo_id, access_key):
#     attachment = f'photo{owner_id}_{photo_id}_{access_key}'
#     vk.messages.send(
#         random_id=get_random_id(),
#         peer_id=peer_id,
#         attachment=attachment
#     )

import sqlite3
date_remainder=""
time_remainder=""
now = datetime.datetime.now()
default_datetime_remainder = now.replace(hour=0, minute=0, second=0, microsecond=0, day=1, month=1, year=1950)

async def bot(event):
    global date_remainder
    global time_remainder
    global counter
    global default_datetime_remainder
    if event.type == VkBotEventType.MESSAGE_NEW:
        print("ggggggggggg")
        message=event.object.message.get('text').lower()
        a=list(event.object.values())[0].get('from_id')
        print(a)
        if re.match('jarvis ', message) or re.match('джарвиз ',message) or re.match('jarvis, ',message) or re.match('джарвиз, ',message) or re.match('jarvis',message) or re.match('джарвиз', message):
            print("ddddddddddddddddd")
            if re.search('привет', message) or re.search('hi', message):
                print("kkkkkkkkkkkkkkkkkkk")
                if event.from_chat:
                    #print(event.client_info)
                    send('Привет!', event.chat_id)
            elif re.search('спасибо', message):
                if event.from_chat:
                    print(event.chat_id)
                    send('Нет проблем!Рад стараться!', event.chat_id)
            # elif re.search("photo", message):
            #     if event.from_chat:
            #         send_photo(vk, event.chat_id, *upload_photo(upload, 'U.png'))
            elif re.search('дай анекдот', message):
                if event.from_chat:
                    async with aiohttp.ClientSession() as session:
                        url = 'https://anekdotov.net/students/'
                        response = await session.get(url)
                        ans=await response.text()
                    soup = BeautifulSoup(ans, 'html.parser')
                    quotes = soup.find_all('div', class_='anekdot')
                    print(quotes[counter].text)
                    send_message=quotes[counter].text
                    counter += 1
                    print("counter: ", counter)
                    send(send_message, event.chat_id)
            elif re.search('создай напоминание', message) or re.search('create a reminder',message):
                #джарвиз, создай напоминание 06-02-2023 15:17 текст напоминания
                if event.from_chat:
                    message = message.replace("jarvis, create a remider", "")
                    message = message.replace("jarvis create a remider", "")
                    message = message.replace("джарвиз, создай напоминание", "")
                    message = message.replace("джарвиз создай напоминание", "")
                    message = message.strip()
                    for i in message:
                        if i != " ":
                            if i=="/" or i=="." or i=="\\" or i==":":
                                i="-"
                            date_remainder+=i
                        while i !=" ":
                            time_remainder+=i
                    date_and_time=date_remainder+" "+time_remainder
                    now_obj = datetime.datetime.strptime(date_and_time, '%d-%m-%Y %H:%M')
                    if now_obj>default_datetime_remainder:
                        default_datetime_remainder=now_obj
            elif re.search('расписание', message) or re.search('timetable',message):
                weekday=datetime.datetime.today().weekday()
                week=datetime.datetime.today().isocalendar()[1]-5
                print(week)
                url="https://ssau.ru/rasp?groupId=530994164&selectedWeek="+str(week)+"&selectedWeekday=1"
                if event.from_chat:
                    async with aiohttp.ClientSession() as session:
                        response = await session.get(url)
                        ans = await response.text()
                    soup = BeautifulSoup(ans, 'html.parser')
                    a = soup.find_all('div', class_='schedule__item')
                    b = soup.find_all('div', class_='schedule__time-item')
                    timetable = []
                    clock=[]
                    for i in b:
                        clock.append(i.text)
                    print(clock)
                    for i in a:
                        timetable.append(i.text)
                    print(timetable)
                    str_timetable=""
                    if weekday==0:
                        weekday=timetable[1]
                        str_timetable=clock[0]+" - "+clock[1]+'\n'+timetable[7]+'\n\n'+clock[2]+" - "+clock[3]+'\n'+timetable[13]+'\n\n'+clock[4]+" - "+clock[5]+'\n'+timetable[19]+'\n\n'+clock[6]+" - "+clock[7]+'\n'+timetable[25]+'\n\n'
                        print(str_timetable)
                    if weekday==1:
                        weekday=timetable[2]
                        str_timetable=clock[0]+" - "+clock[1]+'\n'+timetable[8]+'\n\n'+clock[2]+" - "+clock[3]+'\n'+timetable[14]+'\n\n'+clock[4]+" - "+clock[5]+'\n'+timetable[20]+'\n\n'+clock[6]+" - "+clock[7]+'\n'+timetable[26]+'\n\n'
                        print(str_timetable)
                    if weekday==2:
                        weekday=timetable[3]
                        str_timetable=clock[0]+" - "+clock[1]+'\n'+timetable[9]+'\n\n'+clock[2]+" - "+clock[3]+'\n'+timetable[15]+'\n\n'+clock[4]+" - "+clock[5]+'\n'+timetable[21]+'\n\n'+clock[6]+" - "+clock[7]+'\n'+timetable[27]+'\n\n'
                        print(str_timetable)
                    if weekday==3:
                        weekday=timetable[4]
                        str_timetable=clock[0]+" - "+clock[1]+'\n'+timetable[10]+'\n\n'+clock[2]+" - "+clock[3]+'\n'+timetable[16]+'\n\n'+clock[4]+" - "+clock[5]+'\n'+timetable[22]+'\n\n'+clock[6]+" - "+clock[7]+'\n'+timetable[28]+'\n\n'
                        print(str_timetable)
                    if weekday==4:
                        weekday=timetable[5]
                        str_timetable=clock[0]+" - "+clock[1]+'\n'+timetable[11]+'\n\n'+clock[2]+" - "+clock[3]+'\n'+timetable[17]+'\n\n'+clock[4]+" - "+clock[5]+'\n'+timetable[23]+'\n\n'+clock[6]+" - "+clock[7]+'\n'+timetable[29]+'\n\n'
                        print(str_timetable)
                    if weekday==5:
                        weekday=timetable[6]
                        str_timetable=clock[0]+" - "+clock[1]+'\n'+timetable[12]+'\n\n'+clock[2]+" - "+clock[3]+'\n'+timetable[18]+'\n\n'+clock[4]+" - "+clock[5]+'\n'+timetable[24]+'\n\n'+clock[6]+" - "+clock[7]+'\n'+timetable[30]+'\n\n'
                        print(str_timetable)
                    if weekday==6:
                        weekday="Воскресенье"
                        str_timetable="Сегодня пар нет)))\nМожно отдыхать\n"
                    send(f"Сегодня {weekday}", event.chat_id)
                    send(str_timetable, event.chat_id)
            else:
                if event.from_chat:
                    send('Я не понимаю', event.chat_id)



async def main():
    for event in longpoll.listen():
        try:
            await bot(event)
        except vk_api.exceptions.ApiError:
            continue




if __name__=='__main__':
    asyncio.run(main())



        #     else:
        #         if message == 'Ку' or message == 'Привет' or message == 'Хай' or message == 'Хелло' or message == 'Хеллоу':
        #             if event.from_chat:
        #                 send('Привет!', event.chat_id)
        #         elif message =='jarvis' or message == 'джарвиз':
        #             if event.from_chat:
        #                 send('Вы меня уже вызывали', event.chat_id)
        #         elif 'Дай анекдот' in str(event):
        #             if event.from_chat:
        #                 session = HTMLSession()
        #                 response = session.get('https://anekdotov.net/students/')
        #                 response.html.render()
        #                 soup = BeautifulSoup(response.text, 'lxml')
        #                 quotes = soup.find_all('div', class_='anekdot')
        #                 print(quotes[counter].text)
        #                 send_message=quotes[counter].text
        #                 counter += 1
        #                 print("counter: ", counter)
        #                 send(send_message, event.chat_id)
        #         elif 'Спасибо, Jarvis' in str(event):
        #             if event.from_chat:
        #                 send('Это было не сложно', event.chat_id)
        #                 a=0
        #         else:
        #             if event.from_chat:
        #                 send('Извини, но я не понимаю', event.chat_id)
        # except vk_api.exceptions.ApiError:
        #     continue
# elif 'Клавиатура' in str(event):
#     if event.from_chat:
#         vk.messages.send(
#             keyboard = keyboard.get_keyboard(),
#             key = ('ac0b4d2ae4b707cac7ac3981f2942624d2769f0e'),          #ВСТАВИТЬ ПАРАМЕТРЫ
#             server = ('https://lp.vk.com/wh218320118'),
#             ts=('4'),
#             random_id = get_random_id(),
#             message='Держи',
#             chat_id = event.chat_id
#             )
# elif "Quantum" in str(event):
#     session = HTMLSession()
#     response = session.get('https://ru.wikipedia.org/wiki/Квантовая_физика')
#     response.html.render()
#     soup = BeautifulSoup(response.text, 'lxml')
#     quotes = soup.find_all('a','p')
#     print(quotes)
#     vk.messages.send(
#         key=('f25124946931a230031d57ddd73e4e0efcec4b7b'),  # ВСТАВИТЬ ПАРАМЕТРЫ
#         server=('https://lp.vk.com/wh218320118'),
#         ts=('42'),
#         random_id=get_random_id(),
#         message=quotes,
#         chat_id=event.chat_id
#     )