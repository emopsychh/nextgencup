import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()

MOCK_API_URL = os.getenv("MOCK_CHALLENGERMODE_URL", "http://mock-api/tournaments")

async def create_tournament(title: str, description: str, start_time: str) -> str:
    """
    Создаёт турнир через mock-api и возвращает ссылку на турнир.

    :param title: Название турнира
    :param description: Описание турнира
    :param start_time: Время начала турнира (строкой в формате ISO)
    :return: Ссылка на турнир
    """
    payload = {
        "name": title,
        "description": description,
        "game": "csgo"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(MOCK_API_URL, json=payload) as resp:
            if resp.status == 200:
                data = await resp.json()
                tournament_id = data.get("tournament_id")
                if not tournament_id:
                    raise Exception("Mock-API не вернул ID турнира!")
                return f"http://localhost:3000/tournaments/{tournament_id}"
            else:
                raise Exception(f"Ошибка создания турнира: {resp.status} - {await resp.text()}")
