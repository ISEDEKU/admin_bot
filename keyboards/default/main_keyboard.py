from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu_1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔍 Поиск')
        ],
        [
            KeyboardButton(text='📈 Курс')
        ],
        [
            KeyboardButton(text='❓ Помощь')
        ],
    ],
    resize_keyboard=True
)

menu_2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='❌ Завершить поиск ❌')
        ],
    ],
    resize_keyboard=True
)
