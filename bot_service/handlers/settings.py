from aiogram import Router, types, F
from aiogram.types import Message
from keyboards.main import settings_menu_keyboard, main_menu_keyboard

router = Router()

# Хендлер для кнопки "Настройки"
@router.message(F.text == "⚙️ Настройки")
async def show_settings(message: Message):
    await message.answer("Выберите настройку:", reply_markup=settings_menu_keyboard())

# Хендлер для кнопки "Уведомления и напоминания"
@router.message(F.text == "🔔 Уведомления и напоминания")
async def notifications_reminders(message: Message):
    await message.answer("Здесь будет настройка уведомлений и напоминаний. Настроим позже.")

# Хендлер для кнопки "Изменить язык"
@router.message(F.text == "🌐 Изменить язык на английский")
async def change_language(message: Message):
    await message.answer("Язык изменен на английский.")

# Хендлер для кнопки "FAQ"
@router.message(F.text == "ℹ️ Часто задаваемые вопросы (FAQ)")
async def faq(message: Message):
    await message.answer("Часто задаваемые вопросы:\n1. Как использовать бота?\n2. Как настроить уведомления?")

# Хендлер для кнопки "Назад"
@router.message(F.text == "◀️ Назад")
async def back_to_main_menu(message: Message):
    await message.answer("Вы вернулись в главное меню.", reply_markup=main_menu_keyboard())

