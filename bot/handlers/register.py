from aiogram import Router, types, F
from aiogram.types import Message
from bot.database.database import async_session
from bot.database.operations import get_or_create_user
from bot.keyboards.start_kb import get_start_keyboard
from aiogram.types import CallbackQuery
from bot.database.operations import update_steam_id
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.message(F.text == "/start")
async def start_handler(message: Message):
    telegram_id = message.from_user.id
    username = message.from_user.username

    async with async_session() as session:
        user = await get_or_create_user(session, telegram_id, username)

    await message.answer(
    f"👋 Привет, {username or 'игрок'}!\nТы зарегистрирован в системе NextgenCup.",
    reply_markup=get_start_keyboard()
)
    

@router.callback_query(F.data == "bind_steam")
async def send_steam_link(callback: CallbackQuery):
    tg_id = callback.from_user.id

    # 🔗 ВСТАВЬ сюда свою реальную ссылку с Render
    link = f"https://nextgencup-2.onrender.com/auth/steam?tg_id={tg_id}"

    await callback.message.answer(
        "🔗 Нажми на кнопку ниже, чтобы авторизоваться через Steam:",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Войти через Steam", url=link)]
            ]
        )
    )
    await callback.answer()
