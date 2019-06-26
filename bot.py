from telegram.ext import CommandHandler, Updater

import logging

import answer
import secret

from keyboard import keyboard

logging.basicConfig(format = "%(message)s", level = logging.INFO)

class Bot:
    def __init__(self, token, request_kwargs):
        updater    = Updater(token = token, request_kwargs = request_kwargs)
        dispatcher = updater.dispatcher

        handler_start = CommandHandler("start", self.start)

        dispatcher.add_handler(handler_start)

        updater.start_polling()

    def start(self, bot, update):
        bot.send_message(chat_id = update.message.chat_id, text = answer.start)

if __name__ == "__main__":
    request_kwargs = {
            "proxy_url": "socks5://t.geekclass.ru:7777",
            "urllib3_proxy_kwargs": { "username": "geek", "password": "socks" }
        }

    Bot(secret.token, request_kwargs)
