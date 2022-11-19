import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import dotenv_values
from aiogram.contrib.fsm_storage.memory import MemoryStorage

#Получение токена
config = dotenv_values("config/.env")
API_TOKEN = config['API_TOKEN']
ADMIN = int(config['ADMIN'])

#Настройка логов
logging.basicConfig(level=logging.DEBUG)

#Запуск бота и диспатчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())