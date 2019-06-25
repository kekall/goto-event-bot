from telegram.ext import CommandHandler, Updater

import answer
import secret

request_kwargs = { "proxy_url": "socks5://t.geekclass.ru:7777", "urllib3_proxy_kwargs": { "username": "geek", "password": "socks" } }

updater = Updater(token = secret.token, request_kwargs = request_kwargs)
dispatcher = updater.dispatcher

def start(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text = answer.start)

handler_start = CommandHandler("start", start)

dispatcher.add_handler(handler_start)

updater.start_polling()
