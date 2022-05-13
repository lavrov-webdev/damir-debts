from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_start = KeyboardButton('Добавить долг')

greet_kb = ReplyKeyboardMarkup(one_time_keyboard=True)
greet_kb.add(button_start)

button_taxi = KeyboardButton('Такси')
button_refund = KeyboardButton('Отдали')

purpose_kb = ReplyKeyboardMarkup(one_time_keyboard=True)
purpose_kb.add(button_taxi, button_refund)
