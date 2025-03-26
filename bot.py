import requests
import time
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")  # Leer el token desde la variable de entorno
URL_BASE = f"https://api.telegram.org/bot{TOKEN}"

def responder_mensaje(chat_id, mensaje):
    url = f"{URL_BASE}/sendMessage"
        payload = {"chat_id": chat_id, "text": mensaje}
            requests.post(url, json=payload)

            def obtener_mensajes(last_update_id=None):
                url = f"{URL_BASE}/getUpdates"
                    params = {"offset": last_update_id + 1} if last_update_id else {}
                        response = requests.get(url, params=params).json()
                            return response

                            def main():
                                last_update_id = None
                                    print("Bot iniciado...")

                                        while True:
                                                updates = obtener_mensajes(last_update_id)
                                                        if "result" in updates:
                                                                    for update in updates["result"]:
                                                                                    last_update_id = update["update_id"]
                                                                                                    if "message" in update and "text" in update["message"]:
                                                                                                                        chat_id = update["message"]["chat"]["id"]
                                                                                                                                            text = update["message"]["text"]
                                                                                                                                                                print(f"Mensaje recibido: {text}")

                                                                                                                                                                                    if text.lower() == "/start":
                                                                                                                                                                                                            responder_mensaje(chat_id, "¡Hola! Estoy funcionando.")
                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                        responder_mensaje(chat_id, f"Recibí tu mensaje: {text}")

                                                                                                                                                                                                                                                                time.sleep(2)  # Evita hacer demasiadas peticiones seguidas

                                                                                                                                                                                                                                                                if __name__ == "__main__":
                                                                                                                                                                                                                                                                    main()