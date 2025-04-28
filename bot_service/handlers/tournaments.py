from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from bot_service.keyboards.main import submenu_keyboard
from bot_service.keyboards.tournaments import tournaments_menu_keyboard
from bot_service.keyboards.common import cancel_back_keyboard

from bot_service.db_container.db import AsyncSessionLocal
from bot_service.db_container.models import Tournament
from bot_service.services.mock_api import create_tournament
from bot_service.utils.calendar import generate_calendar

from datetime import datetime, time

router = Router()

class TournamentStates(StatesGroup):
    title = State()
    description = State()
    date = State()
    time = State()

@router.message(F.text == "🏆 Турниры")
async def show_tournaments_section(message: Message):
    await message.answer("📋 Меню турниров:", reply_markup=tournaments_menu_keyboard())

@router.message(F.text == "➕ Создать турнир")
async def start_tournament_creation(message: Message, state: FSMContext):
    await message.answer("🔹 Введите название турнира:", reply_markup=cancel_back_keyboard())
    await state.set_state(TournamentStates.title)

@router.message(TournamentStates.title)
async def set_title(message: Message, state: FSMContext):
    if message.text.lower() in ["назад", "отмена", "❌ отмена"]:
        await cancel_creation(message, state)
        return
    await state.update_data(title=message.text)
    await message.answer("🔹 Введите описание турнира:", reply_markup=cancel_back_keyboard())
    await state.set_state(TournamentStates.description)

@router.message(TournamentStates.description)
async def set_description(message: Message, state: FSMContext):
    if message.text.lower() in ["назад", "отмена", "❌ отмена"]:
        await cancel_creation(message, state)
        return
    await state.update_data(description=message.text)
    await message.answer(
        "📅 Выберите дату начала турнира:",
        reply_markup=generate_calendar()
    )
    await state.set_state(TournamentStates.date)

@router.callback_query(TournamentStates.date)
async def calendar_handler(callback: CallbackQuery, state: FSMContext):
    data = callback.data
    if data == "cancel_calendar":
        await cancel_creation(callback.message, state)
        return

    if data.startswith("day"):
        _, year, month, day = data.split(":")
        selected_date = datetime(int(year), int(month), int(day))
        now = datetime.now()

        # Если выбрана прошлая дата
        if selected_date.date() < now.date():
            await callback.answer("⛔ Вы не можете выбрать прошедшую дату!", show_alert=True)
            return

        await state.update_data(selected_date=selected_date.strftime("%Y-%m-%d"))
        await callback.message.answer(
            "⏰ Введите время начала турнира в формате ЧЧ:ММ (например, 18:30):",
            reply_markup=cancel_back_keyboard()
        )
        await state.set_state(TournamentStates.time)
    elif data.startswith("prev_month") or data.startswith("next_month"):
        direction, year, month = data.split(":")
        year = int(year)
        month = int(month)

        if direction == "prev_month":
            month -= 1
            if month < 1:
                month = 12
                year -= 1
        else:
            month += 1
            if month > 12:
                month = 1
                year += 1

        await callback.message.edit_reply_markup(reply_markup=generate_calendar(year, month))

    await callback.answer()

@router.message(TournamentStates.time)
async def set_time(message: Message, state: FSMContext):
    if message.text.lower() in ["назад", "отмена", "❌ отмена"]:
        await cancel_creation(message, state)
        return

    user_time = message.text.strip()
    try:
        hour, minute = map(int, user_time.split(":"))
        now = datetime.now()

        data = await state.get_data()
        selected_date_str = data.get("selected_date")
        selected_date = datetime.strptime(selected_date_str, "%Y-%m-%d")

        start_datetime = datetime.combine(selected_date.date(), time(hour, minute))

        if start_datetime < now:
            await message.answer(
                "⛔ Нельзя назначить время в прошлом. Введите корректное время:",
                reply_markup=cancel_back_keyboard()
            )
            return

        await state.update_data(start_time=start_datetime.strftime("%Y-%m-%d %H:%M"))

        # Создание турнира
        await create_tournament_from_state(message, state)
        await state.clear()
    except Exception:
        await message.answer(
            "⚠️ Неверный формат времени. Введите снова в формате ЧЧ:ММ (например, 18:30):",
            reply_markup=cancel_back_keyboard()
        )

async def create_tournament_from_state(message: Message, state: FSMContext):
    data = await state.get_data()
    title = data.get("title")
    description = data.get("description")
    start_time_str = data.get("start_time")

    start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")

    try:
        chall_url = await create_tournament(title, description, start_time.isoformat())

        async with AsyncSessionLocal() as session:
            new_tournament = Tournament(
                title=title,
                description=description,
                date=start_time,
                chall_url=chall_url,
                is_active=True
            )
            session.add(new_tournament)
            await session.commit()

        await message.answer(
            text=(
                f"✅ Турнир создан!\n\n"
                f"📌 Название: {title}\n"
                f"📝 Описание: {description}\n"
                f"🕒 Дата начала: {start_time.strftime('%d.%m.%Y %H:%M')}\n"
                f"🔗 [Открыть турнир]({chall_url})"
            ),
            parse_mode="Markdown",
            reply_markup=tournaments_menu_keyboard()
        )
    except Exception as e:
        await message.answer(f"❌ Ошибка создания турнира: {str(e)}")

@router.message(F.text.in_(["❌ Отмена", "◀️ Назад"]))
async def cancel_creation(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "❌ Создание турнира отменено.\n\n📋 Выберите действие:",
        reply_markup=submenu_keyboard()
    )
