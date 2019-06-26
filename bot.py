from telegram.ext import *

import logging

import answer
import secret

import knowmyname

from keyboard import *
from user     import *

logging.basicConfig(format = "%(message)s", level = logging.INFO)

class Bot:
    def __init__(self, token, request_kwargs):
        self.users = []

        updater    = Updater(token = token, request_kwargs = request_kwargs)
        dispatcher = updater.dispatcher

        handler_start      = CommandHandler("start",      self.start)
        handler_play       = CommandHandler("play",       self.play)
        handler_understand = MessageHandler(Filters.text, self.understand)

        dispatcher.add_handler(handler_start)
        dispatcher.add_handler(handler_play)
        dispatcher.add_handler(handler_understand)

        updater.start_polling()

    def start(self, bot, update):
        self.users.append(User(update.message.chat_id))
        bot.send_message(chat_id = update.message.chat_id, text = answer.start)

    def play(self, bot, update):
        user = get_user(self.users, update.message.chat_id)

        if not user.playing:
            game = knowmyname
            user.playing = ["knowmyname", 0, 0, None]
            game.play(user, bot, update)
        else:
            bot.send_message(user.chat_id, playing)

    def understand(self, bot, update):
        user = get_user(self.users, update.message.chat_id)

        if user.playing:
            games[user.playing[0]].play(user, bot, update)
        else:
            bot.send_message(user.chat_id, answer.unknown)

games = {
    "knowmyname": knowmyname
}

if __name__ == "__main__":
    request_kwargs = {
        "proxy_url": "socks5://t.geekclass.ru:7777",
        "urllib3_proxy_kwargs": { "username": "geek", "password": "socks" }
    }

    Bot(secret.token, request_kwargs)
