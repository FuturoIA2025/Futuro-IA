import telebot
import os
from dotenv import load_dotenv

# 🔹 Cargar variables de entorno desde .env
load_dotenv()
TOKEN = os.getenv("7807962142:AAE5dkfA8y7T5YylhUuNWZuI5lq2R0FpPAs")  # 🔹 Obtiene el token desde .env

bot = telebot.TeleBot(TOKEN)

print("Bot iniciado...")
print("Esperando mensajes...")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "¡Hola! Soy tu bot.")

    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        bot.reply_to(message, f"Dijiste: {message.text}")

        bot.polling(none_stop=True, timeout=60)