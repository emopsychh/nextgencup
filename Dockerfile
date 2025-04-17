FROM python:3.13-alpine

WORKDIR /app

# Копируем зависимости
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


# Копируем весь проект
COPY . .

# Точка входа
CMD ["python", "bot_service/main.py"]