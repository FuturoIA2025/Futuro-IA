import telebot
import os
from dotenv import load_dotenv

# 🔹 Cargar variables de entorno desde .env
load_dotenv()

# 🔹 Obtener el token desde la variable de entorno
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Aquí va el nombre de la variable, NO el token directo

# 🔹 Verificar si el token se está cargando correctamente
if not TOKEN:
    raise ValueError("❌ ERROR: No se encontró el TOKEN. Revisa tu archivo .env")

    bot = telebot.TeleBot(TOKEN)

    print("✅ Bot iniciado correctamente")
    print("📩 Esperando mensajes...")

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "¡Hola! Soy tu bot.")

        @bot.message_handler(func=lambda message: True)
        def echo_all(message):
            bot.reply_to(message, f"Dijiste: {message.text}")

            bot.polling(none_stop=True, timeout=60)