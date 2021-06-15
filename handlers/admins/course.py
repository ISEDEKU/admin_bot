import requests
from aiogram import types
from bs4 import BeautifulSoup

from data.config import ADMINS
from keyboards.default.main_keyboard import menu_1
from loader import dp


@dp.message_handler(text='📈 Курс', user_id=ADMINS)
async def course(message: types.Message):
    URL = 'https://minfin.com.ua/company/privatbank/currency/'
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
        'accept': '*/*'
    }

    get_html = requests.get(URL, HEADERS)
    get_content = get_html.text
    soup = BeautifulSoup(get_content, features="html.parser")
    table = soup.find('table', {'class': 'currency-data'})
    td = table.findAll('td')
    td = td[6]
    td = td.text
    td = td[1:8]
    sale_USD = f'USD по курсу {td} UAH'
    await message.answer(f'Актуальный курс на cейчас:\n{sale_USD}', reply_markup=menu_1)
