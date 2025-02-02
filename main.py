import telebot
from telebot import types
import serjei
import telebotgit
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
def cyber():
    arseniy.cyber()
    
@bot.message_handler(commands= ['hello'])
def hello(message):
    maria.hello(message, bot)

@bot.message_handler(commands=['random_number'])
def vladimir(message):
    vladimir.rand_num(message,bot)


@bot.massage_handler(commands=['graet'])
def info(message):
    bot.send_message(message.chat.id, "_________")

bot.infinity_polling()


