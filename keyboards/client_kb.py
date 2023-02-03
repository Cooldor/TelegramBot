from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton('/Time_of_work + Location 🕒')
b2 = KeyboardButton('/Menu 😋')
b3 = KeyboardButton('/End ❌')
b4 = KeyboardButton('Share your phone number 📱', request_contact=True)
b5 = KeyboardButton('Send your location 📍', request_location=True)
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).add(b3).row(b4, b5)      # also possible method .insert
