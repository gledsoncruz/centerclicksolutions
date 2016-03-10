
# -*- coding: utf-8 -*-
from django.dispatch import receiver

from account.signals import password_changed
from account.signals import user_sign_up_attempt, user_signed_up
from account.signals import user_login_attempt, user_logged_in

from pinax.eventlog.models import log
import telebot
from django.conf import settings

bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)
chat_group_id = settings.TELEGRAM_CHAT_GROUP_ID

@receiver(user_logged_in)
def handle_user_logged_in(sender, **kwargs):
    bot.send_message(chat_group_id,'Usuário: {!s} acabou de logar no sistema.'.format(kwargs.get("user")))
    log(
        user=kwargs.get("user"),
        action="USER_LOGGED_IN",
        extra={}
    )


@receiver(password_changed)
def handle_password_changed(sender, **kwargs):
    bot.send_message(chat_group_id, 'Usuário: {!s} acabou de alterar sua senha.'.format(kwargs.get("user")))
    log(
        user=kwargs.get("user"),
        action="PASSWORD_CHANGED",
        extra={}
    )


@receiver(user_login_attempt)
def handle_user_login_attempt(sender, **kwargs):
    bot.send_message(chat_group_id,'Tentativa de login do usuário: {!s}'.format(kwargs.get("username")))
    log(
        user=None,
        action="LOGIN_ATTEMPTED",
        extra={
            "username": kwargs.get("username"),
            "result": kwargs.get("result")
        }
    )


@receiver(user_sign_up_attempt)
def handle_user_sign_up_attempt(sender, **kwargs):
    log(
        user=None,
        action="SIGNUP_ATTEMPTED",
        extra={
            "username": kwargs.get("username"),
            "email": kwargs.get("email"),
            "result": kwargs.get("result")
        }
    )


@receiver(user_signed_up)
def handle_user_signed_up(sender, **kwargs):
    bot.send_message(chat_group_id,'Usuário: {!s} acabou de se cadastrar no sistema.'.format(kwargs.get("user")))
    log(
        user=kwargs.get("user"),
        action="USER_SIGNED_UP",
        extra={}
    )
