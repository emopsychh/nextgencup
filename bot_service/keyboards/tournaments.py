from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def tournaments_menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="➕ Создать турнир")],
            [KeyboardButton(text="◀️ Назад")]
        ],
        resize_keyboard=True
    )
