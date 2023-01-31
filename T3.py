import telebot
import Config

bot = telebot.TeleBot(Config.TOKEN)


@bot.message_handler(content_types=['text'])
def handler(message):
    while True:
        bot.send_message(message.chat.id, message.text)


#RUN
bot.infinity_polling(skip_pending=True)
