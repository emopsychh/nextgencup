from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📋 Главное меню")],
        ],
        resize_keyboard=True
    )

def submenu_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🧑‍💼 Профиль"), KeyboardButton(text="📊 Статистика")],
            [KeyboardButton(text="🏆 Турниры")],
            [KeyboardButton(text="ℹ️ О проекте")],
        ],
        resize_keyboard=True
    )