import requests

TOKEN = "TU_TELEGRAM_TOKEN"
URL = f"https://api.telegram.org/bot{TOKEN}/"

def get_updates():
    response = requests.get(URL + "getUpdates")
        return response.json()

        def send_message(chat_id, text):
            data = {"chat_id": chat_id, "text": text}
                requests.post(URL + "sendMessage", data=data)

                def main():
                    last_update_id = None
                        while True:
                                updates = get_updates()
                                        if "result" in updates and updates["result"]:
                                                    for update in updates["result"]:
                                                                    update_id = update["update_id"]
                                                                                    chat_id = update["message"]["chat"]["id"]
                                                                                                    text = update["message"]["text"]

                                                                                                                    if update_id != last_update_id:
                                                                                                                                        last_update_id = update_id
                                                                                                                                                            send_message(chat_id, f"Recibí tu mensaje: {text}")

                                                                                                                                                            if __name__ == "__main__":
                                                                                                                                                                main()