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
            [KeyboardButton(text="⚙️ Настройки")],
        ],
        resize_keyboard=True
    )
def settings_menu_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🔔 Уведомления и напоминания")],
            [KeyboardButton(text="🌐 Изменить язык на английский")],
            [KeyboardButton(text="ℹ️ Часто задаваемые вопросы (FAQ)")],
            [KeyboardButton(text="◀️ Назад")],
        ],
        resize_keyboard=True
    )

