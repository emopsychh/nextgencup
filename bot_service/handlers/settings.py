from aiogram import Router, types, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from bot_service.keyboards.main import settings_menu_keyboard, main_menu_keyboard

router = Router()

# Клавиатура для FAQ
def faq_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="❓ Как использовать бота?", callback_data="faq_how_to_use")],
        [InlineKeyboardButton(text="🔔 Как настроить уведомления?", callback_data="faq_notifications")],
        [InlineKeyboardButton(text="💳 Как оплатить подписку?", callback_data="faq_payment")]
    ])

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
    await message.answer("Часто задаваемые вопросы:", reply_markup=faq_keyboard())

# Хендлер для callback от кнопок FAQ
@router.callback_query(F.data.startswith("faq_"))
async def handle_faq_callback(callback: CallbackQuery):
    faq_answers = {
        "faq_how_to_use": "👋 Чтобы начать, просто нажми /start и следуй инструкциям.",
        "faq_notifications": "🔔 Перейди в Настройки → Уведомления и включи нужные параметры.",
        "faq_payment": "💳 Оплата осуществляется через встроенную систему. Выбери 'Подписка' в главном меню.",
    }

    data = callback.data

    if data == "faq_back":
        await callback.message.edit_text("Выберите настройку:", reply_markup=settings_menu_keyboard())
    else:
        answer = faq_answers.get(data, "Вопрос не найден.")
        await callback.message.edit_text(answer, reply_markup=faq_keyboard())
    
    await callback.answer()