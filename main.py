import telebot
from telebot import types
import serjei
import config

admins = [1215240396]
clients = []
#инициализировать бота, команда старт, переменные по хранению пользователя (id)
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['help', 'start'])
def info(message):
    serjei.info(message, admins, bot, types)

bot.infinity_polling()

