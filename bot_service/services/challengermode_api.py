import aiohttp
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv(dotenv_path=".env")

MOCK_API_URL = os.getenv("MOCK_CHALLENGERMODE_URL", "http://mock-api/tournaments")

# Функция для создания турнира через муляжное API
async def create_tournament(title: str, description: str, start_time: str):
    payload = {
        "name": title,
        "description": description,
        "game": "csgo"  
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(MOCK_API_URL, json=payload) as resp:
            if resp.status == 200:
                data = await resp.json()
                tournament_id = data["tournament_id"]
                tournament_url = f"http://localhost:3000/tournaments/{tournament_id}"
                return tournament_url
            else:
                raise Exception(f"Ошибка создания турнира: {resp.status} - {await resp.text()}")
