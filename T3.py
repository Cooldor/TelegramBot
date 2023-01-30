import telebot
import Config

bot = telebot.TeleBot(Config.TOKEN)


@bot.message_handler(content_types=['text'])
def handler(message):
    bot.send_message(message.chat.id, message.text)

#RUN
bot.polling(none_stop=True)
