from aiogram.fsm.state import StatesGroup, State

class SteamBinding(StatesGroup):
    waiting_for_steam_id = State()