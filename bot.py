import requests
import time

TOKEN = "7791864132:AAHwPV7f4BgV4U0tTqnWY1Zv-X9gxwEWeY0"  # Reemplaza con tu token de Telegram
URL_BASE = f"https://api.telegram.org/bot{TOKEN}"

def responder_mensaje(chat_id, mensaje):
    url = f"{URL_BASE}/sendMessage"
        payload = {"chat_id": chat_id, "text": mensaje}
            try:
                    requests.post(url, json=payload)
                        except requests.exceptions.RequestException as e:
                                print(f"Error al enviar mensaje: {e}")

                                def obtener_mensajes(last_update_id=None):
                                    url = f"{URL_BASE}/getUpdates"
                                        params = {"offset": last_update_id + 1} if last_update_id is not None else {}
                                            
                                                try:
                                                        response = requests.get(url, params=params).json()
                                                                return response if "result" in response else {"result": []}
                                                                    except requests.exceptions.RequestException as e:
                                                                            print(f"Error al obtener mensajes: {e}")
                                                                                    return {"result": []}

                                                                                    def main():
                                                                                        last_update_id = None
                                                                                            print("Bot iniciado...")

                                                                                                while True:
                                                                                                        updates = obtener_mensajes(last_update_id)
                                                                                                                
                                                                                                                        for update in updates["result"]:
                                                                                                                                    if "update_id" in update:
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