from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import Config

storage = MemoryStorage()
bot = Bot(Config.TOKEN)
dp = Dispatcher(bot, storage=storage)   # creating special variable for bot activity (bot instance)

