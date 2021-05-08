import emoji
from aiogram import types


from data.config import ADMINS
from keyboards.default.main_keyboard import menu_1
from loader import dp
from parsing.buy import buying_USD
from parsing.sale import sale_USD


@dp.message_handler(text='📈 Курс', user_id=ADMINS)
async def course(message: types.Message):
    await  message.answer(f'Актуальный курс на покупку:\n{buying_USD}', reply_markup=menu_1)
    await  message.answer(f'Актуальный курс на продажу:\n{sale_USD}', reply_markup=menu_1)
