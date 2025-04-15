from aiogram import Router, types, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from sqlalchemy import select
from datetime import datetime

from database.db import AsyncSessionLocal
from database.models import Tournament
from keyboards.tournaments import tournaments_menu_keyboard, admin_tournaments_keyboard

router = Router()

# 👤 Укажи свой Telegram ID
ADMIN_ID = 5829755634


# 📂 Главное подменю турниров
@router.message(F.text == "🏆 Турниры")
async def open_tournaments_menu(message: types.Message):
    is_admin = message.from_user.id == ADMIN_ID
    await message.answer(
        "📂Выберите действие:",
        reply_markup=tournaments_menu_keyboard(is_admin)
    )


# 📋 Список турниров (одним сообщением)
@router.message(F.text == "🗂 Список турниров")
async def show_tournament_list(message: types.Message):
    async with AsyncSessionLocal() as session:
        stmt = select(Tournament).where(Tournament.is_active == True)
        result = await session.execute(stmt)
        tournaments = result.scalars().all()

        if not tournaments:
            await message.answer("❌ Сейчас нет активных турниров.")
            return

        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=t.title, callback_data=f"tournament_{t.id}")]
                for t in tournaments
            ]
        )

        await message.answer(
            "📋 <b>Список актуальных турниров:</b>",
            parse_mode="HTML",
            reply_markup=keyboard
        )


# 🎯 Детали конкретного турнира
@router.callback_query(F.data.startswith("tournament_"))
async def show_tournament_details(callback: CallbackQuery):
    tournament_id = int(callback.data.split("_")[1])

    async with AsyncSessionLocal() as session:
        stmt = select(Tournament).where(Tournament.id == tournament_id)
        result = await session.execute(stmt)
        t = result.scalar_one_or_none()

        if not t:
            await callback.answer("❌ Турнир не найден", show_alert=True)
            return

        text = (
            f"🏆 <b>{t.title}</b>\n"
            f"📅 <b>Дата:</b> {t.date.strftime('%d.%m.%Y %H:%M')}\n"
            f"📝 <b>Описание:</b> {t.description}\n\n"
            f"🔗 <a href='{t.chall_url}'>Принять участие</a>"
        )

        await callback.message.answer(text, parse_mode="HTML", disable_web_page_preview=True)
        await callback.answer()


# ➕ Создание турнира (только админ)
@router.message(F.text == "➕ Создать турнир")
async def create_tournament(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("⛔ У тебя нет прав для создания турниров.")
        return

    async with AsyncSessionLocal() as session:
        tournament = Tournament(
            title="CS2 DUO CUP",
            description="Командный турнир на вылет. Приз — слава и XP!",
            date=datetime(2025, 4, 20, 18, 0),
            chall_url="https://challengermode.com/tournaments/cs2-duocup-20apr"
        )
        session.add(tournament)
        await session.commit()

        await message.answer(f"✅ Турнир «{tournament.title}» создан!")
