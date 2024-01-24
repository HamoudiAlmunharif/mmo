import telebot

bot = telebot.TeleBot('6115681831:AAH-8cjHZD_Az6WmxX83_WDeHayCWQG6D8U')  # استبدل 'TOKEN' بتوكن البوت الخاص بك

@bot.message_handler(commands=['start', 'help'])
def send_welcome_message(message):
    bot.reply_to(message, "مرحبًا! أنا روبوت الترحيب")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
