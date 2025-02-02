from Victor import help

def info(message, admins, bot, types):
    user_id = message.chat.id
    if user_id in admins:
        help(message, admins, types, bot)
    else:
        bot.send_message(message.chat.id, "Вы не админ")