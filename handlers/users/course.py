from aiogram import types


from data.config import ADMINS
from keyboards.default.main_keyboard import menu_1
from loader import dp
from parsing.sale import sale_USD


@dp.message_handler(text='📈 Курс', user_id=ADMINS)
async def course(message: types.Message):
    await  message.answer(f'Актуальный курс на cейчас:\n{sale_USD}', reply_markup=menu_1)
