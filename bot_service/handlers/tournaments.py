from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from bot_service.keyboards.main import submenu_keyboard
from bot_service.keyboards.tournaments import tournaments_menu_keyboard

from bot_service.db_container.db import get_session
from bot_service.db_container.models import Tournament
from sqlalchemy import select
from bot_service.services.challengermode_api import create_tournament

router = Router()

class TournamentStates(StatesGroup):
    title = State()
    description = State()
    date = State()

# Меню "🏆 Турниры"
@router.message(F.text == "🏆 Турниры")
async def show_tournaments_section(message: Message):
    await message.answer("📋 Меню турниров:", reply_markup=tournaments_menu_keyboard())

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
async def set_date_and_create(message: Message, state: FSMContext):
    from datetime import datetime
    user_data = await state.get_data()

    try:
        date = datetime.strptime(message.text, "%d.%m.%Y %H:%M")
    except ValueError:
        await message.answer("⚠️ Неверный формат даты. Попробуй снова: 25.04.2025 18:00")
        return

    try:
        chall_url = await create_tournament(
            title=user_data["title"],
            description=user_data["description"],
            start_time=date.isoformat()
        )
    except Exception as e:
        await message.answer(f"❌ Не удалось создать турнир в Challengermode:\n{e}")
        return

    # Сохраняем в БД
    async for session in get_session():
        new_tournament = Tournament(
            title=user_data["title"],
            description=user_data["description"],
            date=date,
            chall_url=chall_url,
            is_active=True
        )
        session.add(new_tournament)
        await session.commit()

    await message.answer(
        text=(
            f"✅ Турнир создан!\n\n"
            f"📌 <b>Название:</b> {user_data['title']}\n"
            f"📝 <b>Описание:</b> {user_data['description']}\n"
            f"🕒 <b>Дата начала:</b> {date.strftime('%d.%m.%Y %H:%M')}\n"
            f"🔗 <b><a href='{chall_url}'>Открыть турнир в Challengermode</a></b>\n\n"
            f"ℹ️ Посмотреть и изменить детали турнира вы можете в веб-приложении во вкладке <b>«Турниры»</b>."
        ),
        parse_mode="HTML",
        reply_markup=tournaments_menu_keyboard()
    )
    await state.clear()

# ◀️ Назад
@router.message(F.text == "◀️ Назад")
async def back_to_main_menu(message: Message):
    await message.answer("🔙 Возвращаемся в главное меню:", reply_markup=submenu_keyboard())
