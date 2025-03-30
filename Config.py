import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

# Verificar que todas las variables estén definidas
if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID or not HUGGINGFACE_TOKEN:
 raise ValueError("Faltan variables en el archivo .env. Verifica que TELEGRAM_TOKEN, TELEGRAM_CHAT_ID y HUGGINGFACE_TOKEN estén definidos.")