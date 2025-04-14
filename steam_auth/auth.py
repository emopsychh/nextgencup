from fastapi import Request
from fastapi.responses import RedirectResponse, HTMLResponse
from openid.consumer.consumer import Consumer, SUCCESS
from openid.store.memstore import MemoryStore
from urllib.parse import parse_qs, urlparse
import uuid

STEAM_OPENID_URL = "https://steamcommunity.com/openid"
store = MemoryStore()

# Временное хранилище Telegram ID, ожидающих привязку
pending_telegram_ids = {}

def get_consumer(session_id: str):
    return Consumer({}, store)

async def start_steam_auth(tg_id: int):
    session_id = str(uuid.uuid4())
    consumer = get_consumer(session_id)

    auth_request = consumer.begin(STEAM_OPENID_URL)
    redirect_url = auth_request.redirectURL(
        realm="http://localhost:8000",
        return_to=f"http://localhost:8000/auth/steam/callback?session_id={session_id}"
    )

    # Сохраняем Telegram ID для дальнейшей привязки
    pending_telegram_ids[session_id] = tg_id
    return RedirectResponse(redirect_url)

async def handle_steam_response(request: Request):
    # Получаем session_id из query-параметров
    session_id = request.query_params.get("session_id")
    if not session_id or session_id not in pending_telegram_ids:
        return HTMLResponse("❌ Ошибка: session_id не найден")

    consumer = get_consumer(session_id)
    url = str(request.url)
    parsed_url = urlparse(url)
    query_dict = {k: v[0] for k, v in parse_qs(parsed_url.query).items()}

    # Проверяем, что авторизация успешна
    openid_response = consumer.complete(query_dict, url)

    if openid_response.status != SUCCESS:
        return HTMLResponse("❌ Не удалось авторизоваться через Steam")

    # Получаем Steam ID
    claimed_id = openid_response.getDisplayIdentifier()
    steam_id = claimed_id.split("/")[-1]

    # Получаем Telegram ID
    tg_id = pending_telegram_ids.pop(session_id)

    # TODO: здесь сохраняем steam_id + tg_id в базу
    return HTMLResponse(f"✅ Привязка прошла успешно! Steam ID: {steam_id}, Telegram ID: {tg_id}")
