from aiogram import types
from config.bot_config import dp, bot
from keyboards.admin_panel_keyboard_main_menu import admin_panel_keyboard_main_menu

@dp.callback_query_handler(text='main menu')
async def admin_panel_main_menu_callback(callback_query: types.CallbackQuery):
    # Удаляем предыдущие сообщения
    await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
    # Отправляем сообщение с клавиатурой
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=f"Ваш ID: {callback_query.from_user.id}",
                           reply_markup=admin_panel_keyboard_main_menu)
