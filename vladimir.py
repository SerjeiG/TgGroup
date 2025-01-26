import random


def rand_num(message,bot):
    if message.text == "random number":
        num = random.randint(1, 5)
        bot.send_message(message.chat.id, f"Ваше число: {num}")
