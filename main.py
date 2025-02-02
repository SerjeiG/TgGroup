import telebot

import config
from telebot import types

from telebot import types
import serjei
import arseniy
import config
import vladimir

import maria



admins = [1215240396]
clients = []
#инициализировать бота, команда старт, переменные по хранению пользователя (id)
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['help', 'start'])
def info(message):
    serjei.info(message, admins, bot, types)

@bot.message_handler(commands=['cyber'])
def cyber(message):
    arseniy.cyber(message, types, bot)

@bot.message_handler(commands=['random_number'])
def vladimir(message):
    vladimir.rand_num(message,bot)


@bot.message_handler(commands=['graet'])
def info(message):
    bot.send_message(message.chat.id, "_________")

@bot.message_handler(commands=['button'])
def message_url(message):
    import vladislav
    vladislav.message_url(message.chat.id, "button", "Press", "https://store.steampowered.com/", bot)

@bot.message_handler(content_types=['text'])
def hello(message):
    maria.hello(message, bot)

bot.infinity_polling()


