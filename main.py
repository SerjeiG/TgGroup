import telebot


import config

admins = [1215240396]
clients = []
#инициализировать бота, команда старт, переменные по хранению пользователя (id)
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['help', 'start'])
def info(message):
    user_id = message.chat.id
    if user_id in admins:
        help(message)
    else:
        bot.send_message(message.chat.id, "Вы не админ")

@bot.massage_handler(commands=['graet'])
def info(message):
    bot.send_message(message.chat.id, "_________")

bot.infinity_polling()


