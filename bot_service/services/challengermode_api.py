import os
import aiohttp
import time
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CHALLENGERMODE_CLIENT_ID")
REFRESH_KEY = os.getenv("CHALLENGERMODE_REFRESH_KEY")

BASE_URL = "https://publicapi.challengermode.com/graphql"

_token_cache = {
    "access_token": None,
    "expires_at": 0
}

# Получаем access токен
async def get_access_token():
    if _token_cache["access_token"] and _token_cache["expires_at"] > time.time():
        return _token_cache["access_token"]

    async with aiohttp.ClientSession() as session:
        url = "https://auth.challengermode.com/connect/token"  # Новый URL для получения токена

        async with session.post(
            url,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "client_credentials",
                "client_id": CLIENT_ID,
                "client_secret": REFRESH_KEY
            }
        ) as resp:
            if resp.status == 200:
                data = await resp.json()
                access_token = data["access_token"]
                expires_in = data["expires_in"]

                _token_cache["access_token"] = access_token
                _token_cache["expires_at"] = time.time() + expires_in - 10  # с запасом

                return access_token
            else:
                raise Exception(f"Ошибка получения токена: {resp.status} - {await resp.text()}")

# Создаем турнир через GraphQL
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
