from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def tournaments_menu_keyboard(is_admin: bool = False):
    buttons = [
        [KeyboardButton(text="🗂 Список турниров")]
    ]

    if is_admin:
        buttons.append([KeyboardButton(text="➕ Создать турнир")])

    # Добавляем кнопку Назад
    buttons.append([KeyboardButton(text="◀️ Назад")])

    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        input_field_placeholder="Выбери действие с турнирами"
    )

def admin_tournaments_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="➕ Создать турнир", callback_data="create_tournament")]
        ]
    )

def confirm_button():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="✅ Подтвердить")],
            [KeyboardButton(text="❌ Отмена")]
        ],
        resize_keyboard=True
    )