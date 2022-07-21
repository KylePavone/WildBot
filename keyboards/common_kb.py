from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b_1 = KeyboardButton("/Menu")
b_2 = KeyboardButton("/wildberries")
b_3 = KeyboardButton("/lamoda")

common_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

common_keyboard.add(b_1).add(b_2).insert(b_3)
