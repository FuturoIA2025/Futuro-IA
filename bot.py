import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()  # Cargar tokens desde .env

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
URL_BASE = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

# Función para obtener respuestas desde Hugging Face
def obtener_respuesta_IA(mensaje):
    url = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}
data = {"inputs": mensaje}
response = requests.post(url, headers=headers, json=data)
                    
if response.status_code == 200:
return response.json()[0]["generated_text"]
else:
return "No pude procesar tu mensaje en este momento."

                                            # Función para obtener mensajes nuevos de Telegram
def obtener_mensajes(last_update_id=None):
                                                url = f"{URL_BASE}/getUpdates" 
                                                params = {"offset": last_update_id + 1} if last_update_id else {} 
response = requests.get(url, params=params).json()
return response

                                                            # Función para responder en Telegram
                                                            # def responder_mensaje(chat_id, mensaje):url = f"{URL_BASE}/sendMessag
                                                            #   payload = {"chat_id": chat_id, "text": mensaje
                                                            #   requests.post(url, json=payload)

                                                                        # Función principal del bot  def main():
last_update_id = None
print("✅ Bot con IA iniciado en GitHub Codespaces...")

while True
updates = obtener_mensajes(last_update_id)
if "result" in updates:
        for update in updates["result"]:
                last_update_id = update["update_id"]
                if "message" in update and "text" in update["message"]:
chat_id = update["message"]["chat"]["id"]
text = update["message"]["text"]
print(f"📩 Mensaje recibido: {text}")
if text.lower() == "/start":
                                                                                                                                                                                                                                                        responder_mensaje(chat_id, "🤖 ¡Hola! Estoy funcionando con IA.")
                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                    respuesta_ia = obtener_respuesta_IA(text)
                                                                                                                                                                                                                                                                                                                            responder_mensaje(chat_id, respuesta_ia)

                                                                                                                                                                                                                                                                                                                                    time.sleep(2)  # Evita hacer demasiadas peticiones seguidas

                                                                                                                                                                                                                                                                                                                                    if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                                                        main()