from dotenv import load_dotenv
import os

load_dotenv()  # Cargar variables del archivo .env

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

print("TELEGRAM_TOKEN:", TELEGRAM_TOKEN)
print("HUGGINGFACE_TOKEN:", HUGGINGFACE_TOKEN)

URL_BASE = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}"
HEADERS = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_TOKEN')}"}

def obtener_respuesta_IA(mensaje):
    res = requests.post("https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill", headers=HEADERS, json={"inputs": mensaje})
 return res.json()[0]["generated_text"] if res.status_code == 200 else "No pude responder ahora."
def obtener_mensajes(last_id=None):
 return requests.get(f"{URL_BASE}/getUpdates", params={"offset": last_id + 1} if last_id else {}).json()
def responder_mensaje(chat_id, mensaje):
requests.post(f"{URL_BASE}/sendMessage", json={"chat_id": chat_id, "text": mensaje})
def main():
    last_id = None
while True:
 updates = obtener_mensajes(last_id)
for update in updates.get("result", []):
last_id = update["update_id"]
if "text" in update["message"]:
chat_id, text = update["message"]["chat"]["id"], update["message"]["text".
responder_mensaje(chat_id, "🤖 ¡Hola!" if text.lower() == "/start" else obtener_respuesta_IA(text))
time.sleep(2)
if __name__ == "__main__":
 main()                