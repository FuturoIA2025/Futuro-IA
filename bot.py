from config import TELEGRAM_TOKEN
import requests
# URL base de la API de Telegram
URL_BASE = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"
def enviar_mensaje(chat_id, mensaje):
 """ Envía un mensaje a un chat de Telegram """
 url = f"{URL_BASE}/sendMessage"
payload = {"chat_id": chat_id, "text": mensaje}
try:
 response = requests.post(url, json=payload)
response.raise_for_status()  # Lanza un error si la respuesta no es 200
print("✅ Mensaje enviado correctamente.")
except requests.exceptions.RequestException as e:
print(f"❌ Error al enviar mensaje: {e}")
print("✅ Bot listo para enviar mensajes...")
