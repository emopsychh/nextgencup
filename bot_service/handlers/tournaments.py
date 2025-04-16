from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from keyboards.main import submenu_keyboard
from keyboards.tournaments import tournaments_menu_keyboard, active_tournaments_inline_keyboard

from db_container.db import get_session
from db_container.models import Tournament
from sqlalchemy import select

router = Router()

class TournamentStates(StatesGroup):
    title = State()
    description = State()
    date = State()

# Меню "🏆 Турниры"
@router.message(F.text == "🏆 Турниры")
async def show_tournaments_section(message: Message):
    await message.answer("📋 Меню турниров:", reply_markup=tournaments_menu_keyboard())

# 📄 Активные турниры (inline-кнопки)
@router.message(F.text == "📄 Активные турниры")
async def list_active_tournaments(message: Message):
    async for session in get_session():
        try:
            stmt = select(Tournament).where(Tournament.is_active == True)
            result = await session.execute(stmt)
            tournaments = result.scalars().all()

            if not tournaments:
                await message.answer("❌ Активных турниров пока нет.")
                return

            await message.answer(
                "📄 Список активных турниров:",
                reply_markup=active_tournaments_inline_keyboard(tournaments)
            )

        except Exception as e:
            await message.answer(f"⚠️ Ошибка при получении турниров: {e}")

# ➕ Создать турнир (FSM)
@router.message(F.text == "➕ Создать турнир")
async def start_tournament_creation(message: Message, state: FSMContext):
    await message.answer("Введите название турнира:")
    await state.set_state(TournamentStates.title)

@router.message(TournamentStates.title)
async def set_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer("Введите описание турнира:")
    await state.set_state(TournamentStates.description)

@router.message(TournamentStates.description)
async def set_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Введите дату начала турнира (пример: 25.04.2025 18:00):")
    await state.set_state(TournamentStates.date)

@router.message(TournamentStates.date)
async def finish_tournament_creation(message: Message, state: FSMContext):
    from datetime import datetime
    user_data = await state.get_data()
    try:
        date = datetime.strptime(message.text, "%d.%m.%Y %H:%M")
    except ValueError:
        await message.answer("⚠️ Неверный формат даты. Попробуйте ещё раз:")
        return

    async for session in get_session():
        tournament = Tournament(
            title=user_data["title"],
            description=user_data["description"],
            date=date,
            is_active=True
        )
        session.add(tournament)
        await session.commit()

    await message.answer(f"✅ Турнир \"{user_data['title']}\" успешно создан!", reply_markup=tournaments_menu_keyboard())
    await state.clear()

# ◀️ Назад
@router.message(F.text == "◀️ Назад")
async def back_to_main_menu(message: Message):
    await message.answer("🔙 Возвращаемся в главное меню:", reply_markup=submenu_keyboard())
