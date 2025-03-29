import os
from dotenv import load_dotenv  # Importa dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener los tokens
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Verificar que se cargaron correctamente
print("TELEGRAM_TOKEN:", TELEGRAM_TOKEN)
print("HUGGINGFACE_TOKEN:", HUGGINGFACE_TOKEN)
print("CHAT_ID:", CHAT_ID)

# Validar que los tokens existen
if not TELEGRAM_TOKEN:
    raise ValueError("Error: TELEGRAM_TOKEN no está configurado en el entorno")