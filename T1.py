from creat_bot import dp
from aiogram.utils import executor


async def on_startup(_):  # aiogram is asynchron library( better speed and functionality ,bot switches between
    print('Bot is online')  # functions in time of possible delays

from Handlers import client, admin, other

client.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

