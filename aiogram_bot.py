import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

API_TOKEN = '5630975781:AAEORceYCE8oCzISglCYQdSDjaYv_AMQURU'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("""Привет!\nЯ бот команды инженеров Sitronics\nДля просмотра моего функционала, введи свою доменную почту и подтверди её :)""")

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("""пока пусто""")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)