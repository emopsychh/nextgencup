from aiogram import Router, types, F
from aiogram.types import Message
from bot.database.database import async_session
from bot.database.operations import get_or_create_user

router = Router()

@router.message(F.text == "/start")
async def start_handler(message: Message):
    telegram_id = message.from_user.id
    username = message.from_user.username

    async with async_session() as session:
        user = await get_or_create_user(session, telegram_id, username)

    await message.answer(f"👋 Привет, {username or 'игрок'}!\nТы зарегистрирован в системе NextgenCup.")
