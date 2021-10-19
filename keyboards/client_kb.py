from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove - удаляет клавиатуру после использования

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')
# b4 = KeyboardButton('Номер телефона', request_contact=True)
# b5 = KeyboardButton('Отправить где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.row(b1,b2).add(b3)#.row(b4,b5)
