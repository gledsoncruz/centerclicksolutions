# -*- coding: utf-8 -*-
import telebot
from django.conf import settings

bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)
chat_group_id = settings.TELEGRAM_CHAT_GROUP_ID

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

class Telegram_Bot:

  def send_message(self,message):
    bot.send_message(chat_group_id, message)
