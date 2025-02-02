markdown = '''
[text](URL)
'''

def cyber(message, types):
    markup = types.Inline_Keyboard_Markup()
    button1 = types.Inline_Keyboard_Button(text="Dota 2", url="https://www.cybersport.ru/tags/dota-2")
    button2 = types.Inline_Keyboard_Button(text="Counter Strike 2", url="https://www.cybersport.ru/tags/cs2")
    markup.add(button1, button2)

    bot.send_message(message.chat.id, '[Cybersport.ru](https://www.cybersport.ru/)', parse_mode='Markdown', reply_markup=keyboard)
