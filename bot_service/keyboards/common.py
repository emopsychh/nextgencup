from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

def back_button():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="◀️ Назад")]
        ],
        resize_keyboard=True
    )

def menu_with_back(buttons: list[str]):
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=text)] for text in buttons
        ] + [[KeyboardButton(text="◀️ Назад")]],
        resize_keyboard=True
    )