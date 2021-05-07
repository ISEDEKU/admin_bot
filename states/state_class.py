from aiogram.dispatcher.filters.state import StatesGroup, State


class Questions(StatesGroup):
    search_name = State()
    serial_num = State()
