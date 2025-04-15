from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import F
from bot.handlers import menu, tournaments
from aiogram import Router


router = Router()


@router.message(F.text == "🎮 Турниры")
async def show_tournament_menu(msg: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📜 Посмотреть турниры", callback_data="view_tournaments")],
        [InlineKeyboardButton(text="➕ Создать турнир", callback_data="create_tournament")],
    ])
    await msg.answer("Выберите действие с турнирами:", reply_markup=keyboard)