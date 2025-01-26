from telebot import types
def message_url(chat_id, text, button_text, url, bot):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text=button_text, url=url)
    markup.add(button)
    bot.send_message(chat_id, text, reply_markup=markup)
