import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

# Obtener los tokens desde el .env
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKE")  # <-- Corrige aquí
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Verificar que los tokens se están cargando correctamente
print("Hugging Face Token:", HUGGINGFACE_TOKEN)
print("Telegram Bot Token:", TELEGRAM_BOT_TOKEN)