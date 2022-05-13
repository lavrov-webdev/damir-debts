from aiogram.dispatcher.filters.state import StatesGroup, State


class main_state(StatesGroup):
    get_name_state = State()
    get_purpose_state = State()
    get_sum_state = State()