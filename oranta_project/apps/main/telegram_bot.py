import requests
from django.conf import settings

TELEGRAM_BOT_TOKEN = settings.TELEGRAM_BOT_TOKEN
TELEGRAM_CHAT_ID = settings.TELEGRAM_CHAT_ID

def send_to_telegram(message):
    if TELEGRAM_BOT_TOKEN is None or TELEGRAM_CHAT_ID is None:
        raise ValueError("TELEGRAM_BOT_TOKEN или TELEGRAM_CHAT_ID не настроены.")
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML",
    }
    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.status_code
