from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_load = KeyboardButton('/Download')
button_delete = KeyboardButton('/Delete')
button_close = KeyboardButton('/Close❌')
button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_delete).add(button_close)
