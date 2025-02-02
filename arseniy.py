markdown = '''
[text](URL)
'''

def cyber(message, bot, types, button_text, url, keyboard, chat_id):
    markup = types.Inline_Keyboard_Markup()
    button = types.Inline_Keyboard_Button(text=button_text, url=url)
    markup.add(button)

    bot.send_message(message.chat.id, '[Cybersport.ru](https://www.cybersport.ru/)', parse_mode='Markdown', reply_markup=keyboard)
