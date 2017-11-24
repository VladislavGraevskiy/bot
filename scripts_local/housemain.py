# coding: utf-8
from __future__ import absolute_import, unicode_literals, division, print_function


import requests
URL = 'https://api.telegram.org/bot'
TOKEN = '419867054:AAHDaorcrkdV_4IyAb2PJWu4gftAlmOXW2o'
# data = {'offset': offset  1, 'limit': 0, 'timeout': 0}
while True:
    # message_data = { # формируем информацию для отправки сообщения
    #         'chat_id': update['message']['chat']['id'], # куда отправляем сообщение
    #         'text': "I'm <b>bot</b>", # само сообщение для отправки
    #         'reply_to_message_id': update['message']['message_id'], # если параметр указан, то бот отправит сообщение в reply
    #         'parse_mode': 'HTML' # про форматирование текста ниже
    #     }
    ans = requests.post(URL+TOKEN+'/getUpdates',) # запрос на отправку сообщения
    print(ans.json())


    f = {u'ok': True, u'result': [{u'message': {u'date': 1511383949, u'text': u'hduedhue', u'from': {u'username': u'uladzislaugr', u'first_name': u'Vladislav', u'last_name': u'Graevkiy', u'is_bot': False, u'language_code': u'en', u'id': 161222966}, u'message_id': 14, u'chat': {u'username': u'uladzislaugr', u'first_name': u'Vladislav', u'last_name': u'Graevkiy', u'type': u'private', u'id': 161222966}}, u'update_id': 365666766}]}

    message_data = { # формируем информацию для отправки сообщения
            'chat_id': f['result'][0]['message']['chat']['id'], # куда отправляем сообщение
            'text': "I'm <b>bot</b>", # само сообщение для отправки
            # 'reply_to_message_id': f['result'][0]['message']['message_id'], # если параметр указан, то бот отправит сообщение в reply
            'parse_mode': 'HTML' # про форматирование текста ниже
        }
    try:
        request = requests.post(URL+TOKEN+'/sendMessage', data=message_data) # запрос на отправку сообщения
    except:
        print('Send message error')

    print(request.json())
