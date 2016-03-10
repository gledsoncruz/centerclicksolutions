# -*- coding: utf-8 -*-
import telebot
from django.conf import settings

bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)
chat_group_id = settings.TELEGRAM_CHAT_GROUP_ID

class Telegram_Bot:

  def send_message(self,message):
    bot.send_message(chat_group_id, message)
