import telebot
import answers
import tokens

bot = telebot.TeleBot(tokens.telebot)

@bot.message_handler(content_types = ["text"])
def on_text(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, answers.help)
    else:
        bot.send_message(message.from_user.id, answers.fail)

bot.polling(none_stop = True, interval = 0)
