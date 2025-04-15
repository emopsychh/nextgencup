from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def tournaments_menu_keyboard(is_admin: bool = False):
    buttons = [[KeyboardButton(text="🗂 Список турниров")]]

    if is_admin:
        buttons.append([KeyboardButton(text="➕ Создать турнир")])

    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        input_field_placeholder="Выбери действие"
    )

def admin_tournaments_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="➕ Создать турнир", callback_data="create_tournament")]
        ]
    )