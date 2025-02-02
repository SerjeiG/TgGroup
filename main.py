import telebot
from telebot import types
import serjei
import config
import Victor

admins = [1215240396]
clients = []
#инициализировать бота, команда старт, переменные по хранению пользователя (id)
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['help', 'start'])
def info(message):
    Vhelp = Victor.help(message, admins, types, bot)
    serjei.info(message, Vhelp)

bot.infinity_polling()

