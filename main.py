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
    user_id = message.chat.id
    if user_id in admins:
        help(message)
    else:
        bot.send_message(message.chat.id, "Вы не админ")

@bot.message_handler(commands=['cyber'])
def cyber():
    arseniy.cyber()
    
@bot.message_handler(commands= ['hello'])
def hello(message):
    maria.hello(message, bot)

@bot.message_handler(commands=['random_number'])
def vladimir(message):
    vladimir.rand_num(message,bot)


bot.infinity_polling()


