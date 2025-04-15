from aiogram.fsm.state import StatesGroup, State

class TournamentCreation(StatesGroup):
    title = State()
    description = State()
    date = State()
    confirm = State()  