from dotenv import load_dotenv
import os

# Cargar las variables de entorno del archivo .env
load_dotenv()

# Obtener los tokens
TOKEN = os.getenv("TOKEN")
API_KEY = os.getenv("API_KEY")

print("TOKEN:", TOKEN)  # Para depurar, revisa si imprime el token (borra esto después)
print("API_KEY:", API_KEY)  # Igual para la API key