from aiogram import Router, types, F
from aiogram.types import Message
from bot.database.database import async_session
from bot.database.operations import get_or_create_user
from bot.keyboards.start_kb import get_start_keyboard
from aiogram.fsm.context import FSMContext
from bot.states.steam import SteamBinding
from aiogram.types import CallbackQuery
from bot.database.operations import update_steam_id

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
async def ask_for_steam_id(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("🔗 Пожалуйста, отправь свой Steam ID или ссылку на профиль:")
    await state.set_state(SteamBinding.waiting_for_steam_id)
    await callback.answer()

@router.message(SteamBinding.waiting_for_steam_id)
async def receive_steam_id(message: Message, state: FSMContext):
    steam_input = message.text
    telegram_id = message.from_user.id

    async with async_session() as session:
        await update_steam_id(session, telegram_id, steam_input)

    await message.answer(f"✅ Аккаунт успешно привязан: {steam_input}")
    await state.clear()
