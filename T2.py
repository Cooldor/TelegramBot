import telebot
import Config
import random

from telebot import types

bot = telebot.TeleBot(Config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲Random number🎲")
    item2 = types.KeyboardButton("How are you??👀")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Greetings, {0.first_name}!\nI am <b>{1.first_name}</b>, '
                                      'Experiment Bot for testing functionality.'.format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def test_handler(message):
    if message.chat.type == 'private':
        if message.text == '🎲Random number🎲':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == 'How are you??👀':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Stonks 😊📈", callback_data='good')
            item2 = types.InlineKeyboardButton("Not Stonks😡📉", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Great! And how is your work?', reply_markup=markup)
#        elif message.text == 'Not Stonks':
#            bot.send.message(message.chat.id, 'Awww=(')
        else:
            bot.send_message(message.chat.id, 'This is out of my functionality for now...')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    img = open('Stonks.jpg', 'rb')
    img2 = open('Not stonks 2.jpg', 'rb')
    try:
        if call.message:
            if call.data == 'good':
                bot.send_photo(call.message.chat.id, img)
            elif call.data == 'bad':
                bot.send_photo(call.message.chat.id, img2)

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='How are you??',
                                  reply_markup=None)
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text='❗️THIS IS TESTING NOTIFICATION❗️')

    except Exception as e:
        print(repr(e))


bot.polling(non_stop=True)

