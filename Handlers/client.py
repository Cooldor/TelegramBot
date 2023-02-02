from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Greetings!', reply_markup=kb_client)   # (await) operator works with async only
        await message.delete()    # it waits for the moment until there is free space in the stream to execute the code
    except:
        await message.reply('Communication with BOT in DMS ONLY ---> \nt.me/Botorian_Bot')



# @dp.message_handler(commands=['Time of work'])
async def pizza_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Monday-Friday(9:00-23:00), Saturday-Sunday(11:00-22:00)')


# @dp.message_handler(commands=['Address'])
async def pizza_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'See you soon', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['Menu'])
async def pizza_menu_command(message : types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Time_of_work'])
    dp.register_message_handler(pizza_place_command, commands=['End'])
    dp.register_message_handler(pizza_menu_command, commands=['Menu'])
