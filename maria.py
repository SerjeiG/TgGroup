def hello(message, bot):
    text = message.text
    message.text = ""
    if message.text == "привет":
        bot.send_message(message.chat.id, text="привет!")
    if message.text == "пока":
        bot.send_message(message.chat.id, text="до встречи!")

