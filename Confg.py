import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Cargar las configuraciones con los nombres correctos
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_TOKEN')