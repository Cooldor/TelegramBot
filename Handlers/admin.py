from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardRemove

ID = None


class FSMadmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


# @dp.message_handler(commands=['admin'], is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Waiting for your command, Master!😉', reply_markup=admin_kb.button_case_admin)
    await message.delete()


# @dp.message_handler(commands='download', state=None)
async def cm_start(message : types.Message):
    if message.from_user.id == ID:
        await FSMadmin.photo.set()
        await message.reply('Send a photo')


# @dp.message_handler(state="*", commands='close')
# @dp.message_handler(Text(equals='close', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state=FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply("OK")


@dp.message_handler(commands='Close❌')
async def close_kb(message: types.Message):
    await bot.send_message(message.from_user.id, 'As you wish! Goodbye, Master!😉', reply_markup=ReplyKeyboardRemove())


# @dp.message_handler(content_types=['photo'], state=FSMadmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMadmin.next()
        await message.reply('Now enter the name of dish')


# @dp.message_handler(state=FSMadmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMadmin.next()
        await message.reply('Enter the description')


# @dp.message_handler(state=FSMadmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMadmin.next()
        await message.reply('Now enter the price')


# @dp.message_handler(state=FSMadmin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = str(message.text + '$')

        await sqlite_db.sql_add_command(state)
        await state.finish()
        await bot.send_message(message.from_user.id, 'Success!\nI send your dish to the data base! You can check it by'
                                                     ' checking /menu command😉')


@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} deleted.\nCheck /menu command', show_alert=True)


@dp.message_handler(commands='delete')
async def delete_item(message: types.Message):
    if message.from_user.id == ID:
        read = await sqlite_db.sql_read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nDescription: {ret[2]}\nPrice: {ret[-1]}')
            await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                                   add(InlineKeyboardButton(f'❌Delete the dish - {ret[1]}❌', callback_data=f'del {ret[1]}')))



def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands='download', state=None)
    dp.register_message_handler(cancel_handler, state="*", commands='delete')
    dp.register_message_handler(cancel_handler, Text(equals='delete', ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMadmin.photo)
    dp.register_message_handler(load_name, state=FSMadmin.name)
    dp.register_message_handler(load_description, state=FSMadmin.description)
    dp.register_message_handler(load_price, state=FSMadmin.price)
    dp.register_message_handler(make_changes_command, commands=['admin'], is_chat_admin=True)
#    dp.register_message_handler(del_callback_run, lambda x: x.data and x.data.startswith('del '))
#    dp.register_message_handler(delete_item, commands='delete')
