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

@bot.message_handler(commands= ['hello'])
def hello(message):
    text = message.text
    message.text = ""
    if "привет" in message:
        bot.send_message(message.chat.id, text="привет!")
    if "пока" in message:
        bot.send_message(message.chat.id, text="до встречи!")

bot.infinity_polling()

