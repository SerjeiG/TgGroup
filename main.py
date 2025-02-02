import telebot
import config
from telebot import types

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

@bot.message_handler(commands=['button'])
def message_url(message):
    import vladislav
    vladislav.message_url(message.chat.id, "button", "Press", "https://store.steampowered.com/", bot)

bot.infinity_polling()

