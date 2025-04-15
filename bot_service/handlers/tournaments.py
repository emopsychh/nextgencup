from aiogram import Router, types, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from sqlalchemy import select
from datetime import datetime
from database.db import AsyncSessionLocal
from database.models import Tournament
from keyboards.tournaments import tournaments_menu_keyboard, admin_tournaments_keyboard
from aiogram.fsm.context import FSMContext
from states.tournament_states import TournamentCreation
from datetime import datetime
from keyboards.main import main_menu_keyboard
from services.challengermode_api import create_tournament
from keyboards.tournaments import confirm_button

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


# START FSM
@router.message(F.text == "➕ Создать турнир")
async def start_tournament_creation(message: types.Message, state: FSMContext):
    if message.from_user.id != ADMIN_ID:
        await message.answer("⛔ У тебя нет прав для создания турниров.")
        return

    await message.answer("📝 Введи <b>название</b> турнира:", parse_mode="HTML")
    await state.set_state(TournamentCreation.title)

#NAME
@router.message(TournamentCreation.title)
async def set_title(message: types.Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer("✏️ Введи <b>описание</b> турнира:", parse_mode="HTML")
    await state.set_state(TournamentCreation.description)

#DESCRIPTION
@router.message(TournamentCreation.description)
async def set_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("📅 Введи <b>дату и время</b> турнира (пример: 20.04.2025 18:00):", parse_mode="HTML")
    await state.set_state(TournamentCreation.date)

#DATE AND TIME
@router.message(TournamentCreation.date)
async def set_date(message: types.Message, state: FSMContext):
    # Получаем данные о турнире
    date = message.text  # Дата, которую ввёл пользователь
    await state.update_data(date=date)

    # Переходим на следующий шаг — Подтверждение
    await message.answer("✅ Подтвердите создание турнира:", reply_markup=confirm_button())
    await state.set_state(TournamentCreation.confirm)


@router.message(TournamentCreation.confirm)
async def confirm_creation(message: types.Message, state: FSMContext):
    if message.text != "✅ Подтвердить":
        await message.answer("❌ Создание отменено.", reply_markup=main_menu_keyboard())
        await state.clear()
        return

    data = await state.get_data()
    title = data["title"]
    description = data["description"]
    start_time = data["date"]  # формат должен быть ISO 8601

    try:
        tournament_url = await create_tournament(title, description, start_time)
        await message.answer(
            f"✅ Турнир создан!\n\n🔗 <a href='{tournament_url}'>Смотреть на Challengermode</a>",
            parse_mode="HTML",
            reply_markup=main_menu_keyboard()
        )
    except Exception as e:
        await message.answer(f"⚠️ Ошибка при создании турнира: {e}", reply_markup=main_menu_keyboard())

    await state.clear()
