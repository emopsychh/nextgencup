from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def cancel_back_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="◀️ Назад"),
                KeyboardButton(text="❌ Отмена")
            ]
        ],
        resize_keyboard=True
    )
