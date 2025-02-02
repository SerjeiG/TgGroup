markdown = '''
[text](URL)
'''

def cyber(message, types, bot):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Dota 2", url="https://www.cybersport.ru/tags/dota-2")
    button2 = types.InlineKeyboardButton(text="Counter Strike 2", url="https://www.cybersport.ru/tags/cs2")
    markup.add(button1, button2)

    bot.send_message(message.chat.id, '[Cybersport.ru](https://www.cybersport.ru/)', reply_markup=markup)
