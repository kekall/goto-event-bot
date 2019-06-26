from telegram import ReplyKeyboardMarkup, KeyboardButton

keyboard = lambda buttons: ReplyKeyboardMarkup(
        [[KeyboardButton(x) for x in xs] for xs in buttons]
    )
