from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import Dispatcher
from aiogram.types import Message

def settings_menu_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🔔 Уведомления и напоминания")],
            [KeyboardButton(text="🌐 Изменить язык на английский")],
            [KeyboardButton(text="❌ Удалить аккаунт")],
            [KeyboardButton(text="ℹ️ Часто задаваемые вопросы (FAQ)")],
            [KeyboardButton(text="◀️ Назад")],
        ],
        resize_keyboard=True
    )

# Хендлер для кнопки "Настройки"
async def show_settings(message: Message):
    await message.answer("Выберите настройку:", reply_markup=settings_menu_keyboard())

async def notifications_reminders(message: Message):
    await message.answer("Здесь будет настройка уведомлений и напоминаний. Настроим позже.")

async def change_language(message: Message):
    await message.answer("Язык изменен на английский.")

async def delete_account(message: Message):
    await message.answer("Ваш аккаунт был удален.")

async def faq(message: Message):
    await message.answer("Часто задаваемые вопросы:\n1. Как использовать бота?\n2. Как настроить уведомления?")

async def back_to_main_menu(message: Message):
    await message.answer("Вы вернулись в главное меню.", reply_markup=settings_menu_keyboard())

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(show_settings, text="⚙️ Настройки")
    dp.register_message_handler(notifications_reminders, text="🔔 Уведомления и напоминания")
    dp.register_message_handler(change_language, text="🌐 Изменить язык на английский")
    dp.register_message_handler(delete_account, text="❌ Удалить аккаунт")
    dp.register_message_handler(faq, text="ℹ️ Часто задаваемые вопросы (FAQ)")
    dp.register_message_handler(back_to_main_menu, text="◀️ Назад")
