from config import TELEGRAM_TOKEN, HUGGINGFACE_TOKEN
import requests

URL_BASE = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

def enviar_mensaje(chat_id, mensaje):
    url = f"{URL_BASE}/sendMessage"
        payload = {"chat_id": chat_id, "text": mensaje}
            requests.post(url, json=payload)

            print("✅ Bot listo para enviar mensajes...")