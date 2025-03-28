import sys
sys.path.append(".")  # Asegura que Python busque en la carpeta actual

from config import TELEGRAM_TOKEN, CHAT_ID 

print("TOKEN:", TELEGRAM_TOKEN)  # Verifica si se importa correctamente

def enviar_mensaje(mensaje):  
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"  
    datos = {"chat_id": CHAT_ID, "text": mensaje}  
    response = requests.post(url, json=datos)  # Usa `json=` en vez de `data=`  
    response.raise_for_status()  

if __name__ == "__main__":  
    enviar_mensaje("¡Hola desde mi bot de Telegram!")