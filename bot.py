import telebot

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, 'Привееет!', parse_mode='html')


bot.polling(none_stop=True)
