import os
import aiohttp
import time
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv(dotenv_path=".env")

CLIENT_ID = os.getenv("CHALLENGERMODE_CLIENT_ID")
REFRESH_KEY = os.getenv("CHALLENGERMODE_REFRESH_KEY")
BASE_URL = "https://publicapi.challengermode.com/graphql"
AUTH_URL = "https://auth.challengermode.com/v1/auth/access_keys"

# Кэш для хранения токена
_token_cache = {
    "access_token": None,
    "expires_at": 0
}


async def get_access_token():
    if _token_cache["access_token"] and _token_cache["expires_at"] > time.time():
        return _token_cache["access_token"]

    async with aiohttp.ClientSession() as session:
        async with session.post(
            AUTH_URL,
            headers={"Content-Type": "application/json"},
            json={
                "refreshKey": REFRESH_KEY
            }
        ) as resp:
            if resp.status == 200:
                data = await resp.json()
                access_token = data["value"]
                expires_at_str = data["expiresAt"]
                expires_at_unix = time.mktime(time.strptime(expires_at_str.split(".")[0], "%Y-%m-%dT%H:%M:%S"))

                _token_cache["access_token"] = access_token
                _token_cache["expires_at"] = expires_at_unix - 10
                return access_token
            else:
                raise Exception(f"Ошибка получения токена: {resp.status} - {await resp.text()}")


# Функция для создания турнира
async def create_tournament(title: str, description: str, start_time: str):
    access_token = await get_access_token()

    query = """
    mutation CreateTournament($title: String!, $description: String!, $startTime: String!) {
        createTournament(input: {
            name: $title,
            description: $description,
            startTime: $startTime,
            gameId: "csgo",  # Заменить на нужный gameId
            platform: "PC",
            region: "EU"
        }) {
            id
            name
            startTime
        }
    }
    """

    variables = {
        "title": title,
        "description": description,
        "startTime": start_time
    }

    # Отправляем запрос на создание турнира
    async with aiohttp.ClientSession() as session:
        async with session.post(
            BASE_URL,
            headers={
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json"
            },
            json={
                "query": query,
                "variables": variables
            }
        ) as resp:
            if resp.status == 200:
                data = await resp.json()
                tournament = data["data"]["createTournament"]
                tournament_url = f"https://challengermode.com/tournaments/{tournament['id']}"
                return tournament_url
            else:
                raise Exception(f"Ошибка создания турнира: {resp.status} - {await resp.text()}")
