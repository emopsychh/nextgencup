from aiogram import Router, types, F
from sqlalchemy.future import select
from db_container.models import User
from db_container.db import AsyncSessionLocal
from aiogram.utils.markdown import hbold

router = Router()

@router.message(F.text == "🧑‍💼 Профиль")
async def show_profile(message: types.Message):
    async with AsyncSessionLocal() as session:
        stmt = select(User).where(User.telegram_id == message.from_user.id)
        result = await session.execute(stmt)
        user = result.scalar_one_or_none()

        if not user:
            await message.answer("Ты не зарегистрирован 🤔 Напиши /start")
            return

        reg_date = user.created_at.strftime("%d.%m.%Y %H:%M") if user.created_at else "неизвестно"

        await message.answer(
            text=(
                f"🧑‍💼 {hbold('Твой профиль')}\n\n"
                f"🆔 ID: {user.telegram_id}\n"
                f"👤 Никнейм: @{user.username or '—'}\n"
                f"🗓 Дата регистрации: {reg_date}\n\n"
                f"🎮 Игр сыграно: {user.games_played}\n"
                f"🏆 Побед: {user.games_won}"
            ),
            parse_mode="HTML"
        )
