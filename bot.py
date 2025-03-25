import os
from dotenv import load_dotenv

load_dotenv()  # Carga las variables del archivo .env

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")