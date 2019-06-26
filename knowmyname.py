import os, json, random

from keyboard import *

def play(user, bot, update):
    if user.playing[1] == 0:
        bot.send_message(user.chat_id, text = rules)
        user.playing[1] = 1
    elif user.playing[1] == 4:
        if user.playing[1] != 1 and user.playing[3] == update.message.text:
            user.playing[2] += 1

        bot.send_message(user.chat_id, text = score + str(user.playing[2]))
        user.played.append(user.playing[0])
        user.playing = None
    else:
        if user.playing[1] != 1 and user.playing[3] == update.message.text:
            user.playing[2] += 1

        with open("knowmyname.json") as f:
            pairs = json.loads(f.read())
            names = list(pairs.values())

        photo = random.choice(os.listdir("knowmyname"))
        vars  = random.choices(names, k = 3)
        right = pairs[photo]
        vars.append(right)
        random.shuffle(vars)
        keys = keyboard([vars])

        bot.send_photo(user.chat_id, photo = open(os.path.join("knowmyname", photo), "rb"), reply_markup = keys)

        user.playing[1] += 1
        user.playing[3]  = right

rules    = "TODO: knowmyname rules"
question = "TODO: knowmyname question"
score    = "TODO: knowmyname score: "
