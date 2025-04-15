from fastapi import Request
from fastapi.responses import RedirectResponse, HTMLResponse
from openid.consumer.consumer import Consumer, SUCCESS
from openid.store.memstore import MemoryStore
from urllib.parse import parse_qs, urlparse
import uuid
import httpx

TELEGRAM_BOT_TOKEN = "7527016074:AAHYfO49uKF4uGPBA8sKNgn7_EWQNAe6AXw"

STEAM_OPENID_URL = "https://steamcommunity.com/openid"
store = MemoryStore()
pending_telegram_ids = {}

def get_consumer(session_id: str):
    return Consumer({}, store)

async def start_steam_auth(tg_id: int):
    session_id = str(uuid.uuid4())
    consumer = get_consumer(session_id)
    auth_request = consumer.begin(STEAM_OPENID_URL)

    redirect_url = auth_request.redirectURL(
        realm="https://nextgencup-steam.onrender.com",
        return_to=f"https://nextgencup-steam.onrender.com/auth/steam/callback?session_id={session_id}"
    )

    pending_telegram_ids[session_id] = tg_id
    return RedirectResponse(redirect_url)

async def handle_steam_response(request: Request):
    session_id = request.query_params.get("session_id")
    if not session_id or session_id not in pending_telegram_ids:
        return HTMLResponse("❌ session_id не найден")

    consumer = get_consumer(session_id)
    url = str(request.url)
    query_dict = {k: v[0] for k, v in parse_qs(urlparse(url).query).items()}

    openid_response = consumer.complete(query_dict, url)

    if openid_response.status != SUCCESS:
        return HTMLResponse("❌ Не удалось авторизоваться через Steam")

    claimed_id = openid_response.getDisplayIdentifier()
    steam_id = claimed_id.split("/")[-1]
    tg_id = pending_telegram_ids.pop(session_id)

    # ✅ Отправим сообщение в Telegram
    async with httpx.AsyncClient() as client:
        await client.post(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            json={
                "chat_id": tg_id,
                "text": f"✅ Вы успешно привязали Steam!\nSteam ID: {steam_id}"
            }
        )

    return HTMLResponse("✅ Вы можете закрыть это окно.")