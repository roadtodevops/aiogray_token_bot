from aiogram import types

#Клавиатура "Админ панель выбрать роль"
admin_panel_keyboard_take_user_role = types.InlineKeyboardMarkup()
#Кнопка Администратор
ap_btn_tura = types.InlineKeyboardButton('Администратор',
                                         callback_data='take_user_role_admin')
#Кнопка Контент менеджер
ap_btn_turcm = types.InlineKeyboardButton('Контент менеджер',
                                          callback_data='take_user_role_cm')

admin_panel_keyboard_take_user_role.row(ap_btn_tura, ap_btn_turcm)