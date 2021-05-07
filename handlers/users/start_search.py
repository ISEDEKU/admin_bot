from aiogram import types

from data.config import ADMINS
from keyboards.default.main_keyboard import menu_2
from loader import dp
from states.state_class import Questions


@dp.message_handler(text='Поиск', user_id=ADMINS)
async def start_search(message: types.Message):
    await message.answer('Что нужно найти?', reply_markup=menu_2)
    await Questions.search_name.set()  # запуск первого состояния