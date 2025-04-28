from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from bot_service.keyboards.main import submenu_keyboard
from bot_service.keyboards.tournaments import tournaments_menu_keyboard
from bot_service.services.mock_api import create_tournament
from bot_service.db_container.db import AsyncSessionLocal
from bot_service.db_container.models import Tournament
from datetime import datetime

router = Router()

class TournamentStates(StatesGroup):
    title = State()
    description = State()
    date = State()

@router.message(F.text == "🏆 Турниры")
async def show_tournaments_section(message: Message):
    await message.answer("📋 Меню турниров:", reply_markup=tournaments_menu_keyboard())

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
    await state.update_data(start_time=message.text)  # Сохраняем дату в FSM

    try:
        await handle_create_tournament(message, state)  # Здесь вызываем твою функцию
    except Exception as e:
        await message.answer(f"❌ Ошибка создания турнира:\n{str(e)}")

    await state.clear()  # Очищаем FSM

@router.message(F.text == "◀️ Назад")
async def back_to_main_menu(message: Message):
    await message.answer("🔙 Возвращаемся в главное меню:", reply_markup=submenu_keyboard())

# И ниже сюда приклеиваешь handle_create_tournament, который я тебе скинул:
async def handle_create_tournament(message: Message, state: FSMContext):
    """Обработчик создания турнира."""

    data = await state.get_data()
    title = data.get("title")
    description = data.get("description")
    start_time_str = data.get("start_time")

    try:
        start_time = datetime.strptime(start_time_str, "%d.%m.%Y %H:%M")
        chall_url = await create_tournament(title, description, start_time.isoformat())

        async with AsyncSessionLocal() as session:
            new_tournament = Tournament(
                title=title,
                description=description,
                date=start_time,
                chall_url=chall_url,
                is_active=True,
            )
            session.add(new_tournament)
            await session.commit()

        await message.answer(
            f"✅ Турнир создан!\n\n"
            f"📌 Название: {title}\n"
            f"📝 Описание: {description}\n"
            f"🕒 Дата начала: {start_time.strftime('%d.%m.%Y %H:%M')}\n"
            f"🔗 <a href='{chall_url}'>Открыть турнир</a>",
            parse_mode="HTML",
            disable_web_page_preview=True,
        )

    except Exception as e:
        await message.answer(f"❌ Ошибка создания турнира:\n{str(e)}")
