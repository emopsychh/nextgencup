from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎮 Турниры")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите раздел ↓"
)