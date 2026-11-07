import telebot
import random

TOKEN = "9006679300:AAEn6d3nEFieJ0774NpDJlp0nuO8k3DR_SI"

bot = telebot.TeleBot(TOKEN)

numbers = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    numbers[user_id] = random.randint(1, 100)

    bot.send_message(
        user_id,
        "Привет! Я BotSabr! 🤖\n"
        "Я загадал число от 1 до 100.\n"
        "Попробуй угадать!"
    )

@bot.message_handler(func=lambda message: True)
def guess(message):
    user_id = message.chat.id

    if user_id not in numbers:
        bot.send_message(user_id, "Напиши /start для начала игры!")
        return

    try:
        guess_number = int(message.text)

        if guess_number < 1 or guess_number > 100:
            bot.send_message(user_id, "Введи число от 1 до 100!")

        elif guess_number < numbers[user_id]:
            bot.send_message(user_id, "Моё число больше!")

        elif guess_number > numbers[user_id]:
            bot.send_message(user_id, "Моё число меньше!")

        else:
            bot.send_message(
                user_id,
                "🎉 Молодец! Ты угадал!\nНапиши /start для новой игры."
            )
            del numbers[user_id]

    except ValueError:
        bot.send_message(user_id, "Отправь число!")

print("BotSabr запущен!")
bot.infinity_polling()