import os
from dotenv import load_dotenv

# Cargar las variables desde .env
load_dotenv()

# Obtener los valores de las variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")