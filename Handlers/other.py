import json, string
from aiogram import types, Dispatcher
from create_bot import dp


#@dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation))for i in message.text.split(' ')}.intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('swearing is forbidden')
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
