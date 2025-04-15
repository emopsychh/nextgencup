from aiogram import Router, F
from aiogram.types import Message
from bot.keyboards.main import main_menu_kb

router = Router()

@router.message(F.text == "/start")
async def welcome(msg: Message):
    await msg.answer("Добро пожаловать в NextgenCup!\nВы успешно зарегистрированы и привязали Steam.", reply_markup=main_menu_kb)