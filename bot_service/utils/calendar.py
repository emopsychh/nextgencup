from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
import calendar

def generate_calendar(year: int = None, month: int = None) -> InlineKeyboardMarkup:
    now = datetime.now()
    if not year:
        year = now.year
    if not month:
        month = now.month

    today = now.date()
    inline_keyboard = []

    # Шапка с месяцем и стрелками
    inline_keyboard.append([
        InlineKeyboardButton(text="<<", callback_data=f"prev_month:{year}:{month}"),
        InlineKeyboardButton(text=f"{calendar.month_name[month]} {year}", callback_data="ignore"),
        InlineKeyboardButton(text=">>", callback_data=f"next_month:{year}:{month}")
    ])

    # Дни недели
    week_days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    inline_keyboard.append([
        InlineKeyboardButton(text=day, callback_data="ignore") for day in week_days
    ])

    # Дни месяца
    month_calendar = calendar.monthcalendar(year, month)
    for week in month_calendar:
        row = []
        for day in week:
            if day == 0:
                row.append(InlineKeyboardButton(text=" ", callback_data="ignore"))
            else:
                day_date = datetime(year, month, day).date()
                if day_date < today:
                    row.append(InlineKeyboardButton(text="🚫", callback_data="ignore"))
                else:
                    row.append(InlineKeyboardButton(text=str(day), callback_data=f"day:{year}:{month}:{day}"))
        inline_keyboard.append(row)

    # Кнопка отмены
    inline_keyboard.append([
        InlineKeyboardButton(text="❌ Отмена", callback_data="cancel_calendar")
    ])

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
