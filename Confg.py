from dotenv import load_dotenv
import os
# Cargar variables de entorno
load_dotenv()
# Obtener los tokens
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
# Validar que los tokens existen
if not TELEGRAM_TOKEN:
raise ValueError("Error: TELEGRAM_TOKEN no está configurado en el entorno.")
if not HUGGINGFACE_TOKEN:
raise ValueError("Error: HUGGINGFACE_TOKEN no está configurado en el entorno.")
print("✅ Configuración cargada correctamente.")   