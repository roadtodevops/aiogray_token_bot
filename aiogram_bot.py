import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import dotenv_values

#Получение токена
config = dotenv_values(".env")
API_TOKEN = config['API_TOKEN']

#Настройка логов
logging.basicConfig(level=logging.DEBUG)

#Запуск бота и диспатчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#Запуск приветствия
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("""Привет!\nЯ бот команды инженеров Sitronics\nДля просмотра моего функционала, введи свою доменную почту и подтверди её :)""")

#
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("""пока пусто""")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)