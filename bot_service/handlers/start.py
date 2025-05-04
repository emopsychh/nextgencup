# bot_service/handlers/start.py

from aiogram import Router, types, F
from aiogram.filters import CommandStart
from sqlalchemy.future import select

from bot_service.db_container.db import AsyncSessionLocal
from bot_service.db_container.models import User
from bot_service.keyboards.main import main_menu_keyboard, submenu_keyboard

router = Router()

@router.message(CommandStart())
async def register_user(message: types.Message):
    async with AsyncSessionLocal() as session:
        stmt = select(User).where(User.telegram_id == message.from_user.id)
        result = await session.execute(stmt)
        user = result.scalar_one_or_none()

        if not user:
            # используем message.bot вместо импорта bot из main!
            photos = await message.bot.get_user_profile_photos(message.from_user.id)    
            photo_file_id = None
            if photos.total_count > 0 and photos.photos:
                photo_file_id = photos.photos[0][0].file_id

            user = User(
                telegram_id=message.from_user.id,
                username=message.from_user.username,
                photo_url=photo_file_id,
            )
            session.add(user)
            await session.commit()

            await message.answer(
                text=(
                    f"👋 Привет, {message.from_user.full_name}!\n"
                    "Ты успешно зарегистрирован в системе NextgenCup 🏆\n\n"
                    "В скором времени здесь появятся матчи, турнирные таблицы и многое другое!"
                ),
                reply_markup=main_menu_keyboard()
            )
        else:
            await message.answer(
                text="👋 Ты уже зарегистрирован",
                reply_markup=main_menu_keyboard()
            )

#О проекте
@router.message(F.text == "ℹ️ О проекте")
async def about_project(message: types.Message):
    await message.answer(
        "🧠 *NextgenCup* — это турнирная платформа для CS2 🎮\n\n"
        "🔹 Участвуй в турнирах\n"
        "🔹 Следи за своей статистикой\n"
        "🔹 Собирай команду и побеждай!\n\n"
        "Всё через Telegram — просто, удобно и быстро!",
        parse_mode="Markdown"
    )

# 📋 Главное меню
@router.message(F.text == "📋 Главное меню")
async def open_main_menu(message: types.Message):
    await message.answer(
        text="👇 Выберите действие:",
        reply_markup=submenu_keyboard()
    )