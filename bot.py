from config import TELEGRAM_TOKEN, CHAT_ID
print("TOKEN:", TELEGRAM_TOKEN)  # Para ver si se importa correctamente
def enviar_mensaje(mensaje):
 url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
datos = {"chat_id": CHAT_ID, "text": mensaje}
response = requests.post(url, data=datos)
response.raise_for_status()
if __name__ == "__main__":
 enviar_mensaje("¡Hola desde mi bot de Telegram!")