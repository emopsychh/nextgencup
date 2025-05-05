# NextgenCup 🏆

**NextgenCup** — платформа для проведения турниров по Counter-Strike 2 с использованием Telegram-бота и веб-интерфейса.

## 📦 Структура проекта

```
nextgencup/
├── bot/               # Telegram-бот (Aiogram)
├── backend/           # API (FastAPI или Flask)
├── web/               # Веб-интерфейс (Next.js)
├── db/                # SQL-модели, миграции
├── docs/              # Документация и ТЗ
├── .gitignore
├── README.md
```

## 🚀 MVP-функции
- Регистрация игроков и команд через Telegram-бот
- Участие в турнирах
- Веб-интерфейс
- Создание турниров

## 🛠️ Стек технологий
- Python (Aiogram, FastAPI/Flask)
- React / Next.js
- PostgreSQL / SQLite
- [Макет в Figma](https://www.figma.com/board/aQ2wJjgAqv5F4tHpTRYiTr/Untitled?node-id=0-1&t=n0QZH3CfRSOWJjeo-1)

## 🧪 Установка
```bash
git clone https://github.com/your-org/nextgencup.git
cd nextgencup
# запуск отдельных компонентов в их директориях
```

## ▶️ Запуск проекта

Для запуска всех компонентов проекта с использованием Docker:

```bash
# Убедитесь, что Docker и Docker Compose установлены
docker-compose up --build
```

Или по отдельности вручную:

### 🔹 Backend (FastAPI)
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### 🔹 Telegram-бот
```bash
cd bot
pip install -r requirements.txt
python main.py
```

### 🔹 Web-интерфейс (Next.js)
```bash
cd web
npm install
npm run dev
```

### 💾 Миграции базы данных (если используется Alembic)
```bash
cd db
alembic upgrade head
```

## 🧑‍💻 Команда
- Telegram-бот: [@emopsych](https://t.me/emopsych), [@Lexa_Arbuz](https://t.me/Lexa_Arbuz)
- Веб: [@aaseewaa](https://t.me/aaseewaa), [@SergWz54](https://t.me/SergWz54)
- Backend: [@emopsych](https://t.me/emopsych), [@necroAnkh13](https://t.me/necroAnkh13)

## 📄 Лицензия
MIT License
