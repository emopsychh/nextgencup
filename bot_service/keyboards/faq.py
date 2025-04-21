from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def faq_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="❓ Как использовать бота?", callback_data="faq_how_to_use")],
        [InlineKeyboardButton(text="🔔 Как настроить уведомления?", callback_data="faq_notifications")],
        [InlineKeyboardButton(text="💳 Как оплатить подписку?", callback_data="faq_payment")],
        [InlineKeyboardButton(text="◀️ Назад", callback_data="faq_back")]
    ])