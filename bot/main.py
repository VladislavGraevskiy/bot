# coding: utf-8
from __future__ import absolute_import, unicode_literals, division, print_function

import telepot


TOKEN = '419867054:AAHDaorcrkdV_4IyAb2PJWu4gftAlmOXW2o'

telegram_bot = telepot.Bot(TOKEN)
print (telegram_bot.getUpdates())