from aiogram.dispatcher.filters.state import State, StatesGroup

class RegisterState(StatesGroup):
    prayer = State()
    quran = State()