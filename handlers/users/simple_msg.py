from aiogram import types

from data.config import USERS
from loader import dp


@dp.message_handler(user_id=USERS)
async def simple_msg(message: types.Message):
    await message.answer('Простите, но я не отвечаю на обычные собщения.\nМожет быть вы хотели сделать запрос?')
