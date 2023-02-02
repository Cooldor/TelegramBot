from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token='5840098846:AAHAadx8i0Fm06419vEzh37Rncrlgo75AY8')
dp = Dispatcher(bot, storage=storage)   # creating special variable for bot activity (bot instance)

