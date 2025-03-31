import telebot
import os
import requests
from flask import Flask, request

# Cargar variables de entorno
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")  # Para enviar mensajes automáticos
PORT = int(os.getenv("PORT", 5000))  # Puerto para la API Web

if not TOKEN or not CHAT_ID:
    print("Error: Falta TELEGRAM_TOKEN o TELEGRAM_CHAT_ID en el .env")
    exit()

    bot = telebot.TeleBot(TOKEN)
    app = Flask(__name__)

    # ======= TELEGRAM BOT ======= #

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
     bot.reply_to(message, "¡Hola! Soy tu asistente supremo.")

    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
     bot.reply_to(message, f"Me dijiste: {message.text}")

    # ======= MENSAJE AUTOMÁTICO A TELEGRAM ======= #

    def send_telegram_message(text):
     url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
     data = {"chat_id": CHAT_ID, "text": text}
     response = requests.post(url, json=data)
     return response.json()

     # ======= API WEB (HUGGING FACE) ======= #

    @app.route("/", methods=["GET"])
    def home():
     return "¡Hola! La API está funcionando."

    @app.route("/chat", methods=["POST"])
    def chat():
     data = request.json
     user_message = data.get("message", "")

     if not user_message:
      return {"error": "No se envió ningún mensaje"}, 400

    response_text = f"Me dijiste: {user_message}"

    # Enviar respuesta a Telegram automáticamente
    send_telegram_message(response_text)

   # ======= INICIAR EL BOT ======= #

    if __name__ == "__main__":
      ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

    if ENVIRONMENT == "production":
     print("Iniciando en modo producción (API Web)...")
    app.run(host="0.0.0.0", port=PORT)  # Para Hugging Face/Railway
   
    if mensaje == "Hola":
      print("Hola, ¿cómo estás?")
    else:
     print("No entendí tu mensaje.")
              # Código aquí
    print("Iniciando en modo desarrollo con Telegram...")
    bot.infinity_polling()