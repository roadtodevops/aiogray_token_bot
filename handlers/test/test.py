from aiogram import types
from config.bot_config import dp

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
