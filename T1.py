from create_bot import dp
from aiogram.utils import executor
from data_base import sqlite_db


async def on_startup(_):  # aiogram is asynchron library( better speed and functionality ,bot switches between
    print('Bot is online')  # functions in time of possible delays
    sqlite_db.sql_start()


from Handlers import client, admin, other


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

