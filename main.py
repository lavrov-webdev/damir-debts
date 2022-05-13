from dotenv import load_dotenv
load_dotenv()

import asyncio
from aiogram import executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

import markups
from bot import dp
from states import main_state
from utils import createNewDept, get_users

loop = asyncio.get_event_loop()


@dp.message_handler(Command('start'))
async def send_welcome(message: types.Message):
    await message.reply("Привет. Я помогу быстро записать твой долг Дамиру", reply_markup=markups.greet_kb)


@dp.message_handler(Text(equals="Добавить долг"))
async def add_debt(message: types.Message):
    users_list = get_users()
    users_kb = ReplyKeyboardMarkup(one_time_keyboard=True)
    for key in users_list:
        users_kb.add(KeyboardButton(key))
    await message.answer('Введите имя', reply_markup=users_kb)
    await main_state.get_name_state.set()


@dp.message_handler(state=main_state.get_name_state)
async def get_name_state(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(get_name_state=answer)
    await message.answer('Цель долга', reply_markup=markups.purpose_kb)
    await main_state.get_purpose_state.set()


@dp.message_handler(state=main_state.get_purpose_state)
async def get_name_state(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(get_purpose_state=answer)
    await message.answer('Сумма долга')
    await main_state.get_sum_state.set()


@dp.message_handler(state=main_state.get_sum_state)
async def get_name_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        answer = message.text
        await state.update_data(get_sum_state=answer)
        await message.answer(createNewDept(data['get_name_state'],
                                           data['get_purpose_state'],
                                           answer),
                             reply_markup=markups.greet_kb)
        data.state = None


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, loop=loop)
