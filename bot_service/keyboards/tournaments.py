from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def tournaments_menu_keyboard():
    from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📄 Активные турниры")],
            [KeyboardButton(text="➕ Создать турнир")],
            [KeyboardButton(text="◀️ Назад")]
        ],
        resize_keyboard=True
    )

def active_tournaments_inline_keyboard(tournaments: list) -> InlineKeyboardMarkup:
    buttons = []
    for t in tournaments:
        date = t.date.strftime('%d.%m.%Y') if t.date else "без даты"
        title = f"{t.title} — {date}"
        url = t.chall_url or "https://challengermode.com"
        buttons.append([InlineKeyboardButton(text=title, url=url)])

    return InlineKeyboardMarkup(inline_keyboard=buttons)
