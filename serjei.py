from main import admins, bot


def info(message):
    user_id = message.chat.id
    if user_id in admins:
        help(message)
    else:
        bot.send_message(message.chat.id, "Вы не админ")