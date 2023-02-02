from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_load = KeyboardButton('/download')
button_delete = KeyboardButton('/close')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_delete)