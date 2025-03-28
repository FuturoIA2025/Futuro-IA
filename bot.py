import requests  
from config import TOKEN, CHAT_ID  
def enviar_mensaje(mensaje):  
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"  
datos = {"chat_id": CHAT_ID, "text": mensaje}  
response = requests.post(url, data=datos)  
response.raise_for_status()  # Verifica si hay errores  
if __name__ == "__main__":  
 enviar_mensaje("¡Hola desde mi bot de Telegram!")