from aiogram import types

from data.config import ADMINS
from loader import dp


@dp.message_handler(text='❓ Помощь', user_id=ADMINS)
async def command_help(message: types.Message):
    await message.answer('''
Я бот, который помогает найти информацию о товаре!\n
Чтобы начать поиск, нажми кнопку "Поиск", затем введите название искомого товара.
Вам не обязательно вводить название или атрибут целиком, в таком случае я выведу вам список товаров.
''')
