import requests
from loguru import logger
from core.config import settings

API_URL = f"{settings.django_api_url}/api/telegram-users/"
API_TOKEN = settings.django_api_token

HEADERS = {"Authorization": f"Token {API_TOKEN}"}


def update_or_create_user(id_tg: int, username: str = None) -> bool:
    data = {
        "telegram_id": id_tg,
        "username": username,
    }
    try:
        response = requests.post(API_URL, json=data, headers=HEADERS, timeout=5)
        if response.status_code == 200 or response.status_code== 201:
            return True
        else:
            logger.error(f"[API ERROR] {response.status_code}: {response.text}")
            return False

    except requests.exceptions.RequestException as e:
        logger.exception(f"[API EXCEPTION] Ошибка при запросе к API: {e}")
        return False