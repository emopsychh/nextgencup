from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
import calendar
from zoneinfo import ZoneInfo

def generate_calendar(year: int = None, month: int = None) -> InlineKeyboardMarkup:
    now = datetime.now(ZoneInfo("Europe/Moscow"))
    if not year:
        year = now.year
    if not month:
        month = now.month

    markup = InlineKeyboardMarkup(inline_keyboard=[])

    # Заголовок с кнопками назад / вперед
    markup.inline_keyboard.append([
        InlineKeyboardButton(text="<<", callback_data=f"prev_month:{year}:{month}"),
        InlineKeyboardButton(text=f"{calendar.month_name[month]} {year}", callback_data="ignore"),
        InlineKeyboardButton(text=">>", callback_data=f"next_month:{year}:{month}")
    ])

    # Заголовок дней недели
    markup.inline_keyboard.append([
        InlineKeyboardButton(text="Пн", callback_data="ignore"),
        InlineKeyboardButton(text="Вт", callback_data="ignore"),
        InlineKeyboardButton(text="Ср", callback_data="ignore"),
        InlineKeyboardButton(text="Чт", callback_data="ignore"),
        InlineKeyboardButton(text="Пт", callback_data="ignore"),
        InlineKeyboardButton(text="Сб", callback_data="ignore"),
        InlineKeyboardButton(text="Вс", callback_data="ignore"),
    ])

    # Календарные дни
    month_calendar = calendar.monthcalendar(year, month)
    for week in month_calendar:
        buttons = []
        for day in week:
            if day == 0:
                buttons.append(InlineKeyboardButton(text=" ", callback_data="ignore"))
            else:
                day_date = datetime(year, month, day, tzinfo=ZoneInfo("Europe/Moscow"))
                if day_date.date() < now.date():
                    buttons.append(InlineKeyboardButton(text="❌", callback_data="ignore"))
                else:
                    buttons.append(InlineKeyboardButton(text=str(day), callback_data=f"day:{year}:{month}:{day}"))
        markup.inline_keyboard.append(buttons)

    # Кнопка отмены
    markup.inline_keyboard.append([
        InlineKeyboardButton(text="❌ Отмена", callback_data="cancel_calendar")
    ])

    return markup
