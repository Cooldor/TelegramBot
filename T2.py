import telebot
import Config
import random

from telebot import types
from telebot.types import ReplyKeyboardRemove

bot = telebot.TeleBot(Config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('Images/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id,
                     'Greetings, {0.first_name}!\nI am <b>{1.first_name}</b>,'
                     ' Experiment Bot for testing functionality.\nCommands list:'
                     '\n/start - welcome message + initial activation of the bot.'
                     '\n/help - command list.'
                     '\n/fun - some fun with special Keyboard Buttons. =)'
                     .format(message.from_user, bot.get_me()), parse_mode='html')


@bot.message_handler(commands=['help'])
def help_command(message):
    a_sti = open('Images/9.mp4', 'rb')
    bot.send_animation(message.chat.id, a_sti)
    bot.send_message(message.chat.id, 'Commands list:'
                     '\n/start - welcome message + initial activation of the bot.'
                     '\n/help - command list.'
                     '\n/fun - some fun with special Keyboard Buttons. =)')


@bot.message_handler(commands=['fun'])
def fun_buttons(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲Random number🎲")
    item2 = types.KeyboardButton("How are you??👀")
    item3 = types.KeyboardButton("⛔️END⛔️")

    markup.row(item1, item2, item3)

    bot.send_message(message.chat.id, 'Here we go!😉', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text_handler(message):
    if message.text == '🎲Random number🎲':
        bot.send_message(message.chat.id, str(random.randint(0, 100)))
    elif message.text == 'How are you??👀':
        markup = types.InlineKeyboardMarkup(row_width=3)
        item1 = types.InlineKeyboardButton("Stonks 😊📈", callback_data='good')
        item2 = types.InlineKeyboardButton("Not Stonks😡📉", callback_data='bad')

        markup.add(item1, item2)

        bot.send_message(message.chat.id, 'Great! And how is your work?', reply_markup=markup)
    elif message.text == '⛔️END⛔️':
        bot.send_message(message.chat.id, 'Noooooo... =(', reply_markup=ReplyKeyboardRemove())

#    else:
#        bot.send_message(message.chat.id, "I am scared, I don't understand... "
#                                          "\nIf you want to see my command list - type /help")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline_buttons(call):
    img = open('Images/Stonks.jpg', 'rb')
    img2 = open('Images/Not stonks 2.jpg', 'rb')
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
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                      text='❗️THIS IS TESTING NOTIFICATION❗️')

    except Exception as e:
        print(repr(e))


bot.polling(non_stop=True)
