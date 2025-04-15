from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from keyboards.common import back_button
from keyboards.main import main_menu_keyboard
from states.tournament_states import TournamentCreation

router = Router()


@router.message(F.text == "◀️ Назад")
async def universal_back(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    # 🔁 Возврат по шагам FSM (создание турнира)
    match current_state:
        case TournamentCreation.description.state:
            await message.answer("📝 Введи название турнира снова:", reply_markup=back_button())
            await state.set_state(TournamentCreation.title)

        case TournamentCreation.date.state:
            await message.answer("✏️ Введи описание снова:", reply_markup=back_button())
            await state.set_state(TournamentCreation.description)

        case TournamentCreation.chall_url.state:
            await message.answer("📅 Введи дату и время снова:", reply_markup=back_button())
            await state.set_state(TournamentCreation.date)

        case TournamentCreation.confirm.state:
            await message.answer("🔗 Вставь ссылку снова:", reply_markup=back_button())
            await state.set_state(TournamentCreation.chall_url)

        case _:
            # Не в FSM — вернуться в главное меню
            await state.clear()
            await message.answer("📲 Главное меню", reply_markup=main_menu_keyboard())
