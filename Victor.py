

#@bot.message.handler(commands=["help"])
def help (message, admins, types, bot):
    user_id = [message.chat.id]
    if user_id == admins():
        admin_murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        admin_murkup.add(types.KeyboardButton(text="Изменить текст"))
        admin_murkup.add(types.KeyboardButton(text="Изменить сылку"))
        admin_murkup.add(types.KeyboardButton(text="Показать сообщение"))
        admin_murkup.add(types.KeyboardButton(text="Начать рассылку"))
        admin_murkup.add(types.KeyboardButton(text="Помощь"))
        bot.send_message(message.chat.id, "Команды бота:\n"
                                          "/edit_message - Редактирование сообщения для отправки. \n"
                                          "/edit_link - изменение ссылки для отправки сообщения.\n"
                                          "/show_message - Показать сообщение для отправки.\n"
                                          "/send_message - Написать сообщение для отправки.\n"
                                          "/help - Команда для помощи админу.", reply_markup=admin_murkup)
    else:
        user_murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        user_murkup.add(types.KeyboardButton(text="Рандом"))
        user_murkup.add(types.KeyboardButton(text="Посетить сайт"))
        user_murkup.add(types.KeyboardButton(text="Играть в игры"))
        user_murkup.add(types.KeyboardButton(text="Написать админу"))
        user_murkup.add(types.KeyboardButton(text="Помощь"))
        bot.send_message(message.chat.id, "Команды бота:\n"
                                          "/go_random \n"
                                          "/visit_site\n"
                                          "/game_games\n"
                                          "/message_admin\n"
                                          "/help - Команда для помощи клиента.", reply_markup=admin_murkup)
