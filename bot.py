import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
from Config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, HUGGINGFACE_TOKEN
import requests

# URL del modelo en Hugging Face (puedes cambiarlo si tienes otro modelo)
API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"

# Función para obtener respuesta desde Hugging Face
def get_response_from_huggingface(user_message):
 headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}
 payload = {"inputs": user_message}

 response = requests.post(API_URL, headers=headers, json=payload)

 if response.status_code == 200:
  return response.json()[0]["generated_text"]
 else:
  return "Lo siento, hubo un error procesando tu mensaje."

  # Función de inicio
def start(update, context):
  update.message.reply_text("¡Hola! Soy tu bot de IA. Envíame un mensaje y te responderé con inteligencia artificial.")

  # Función para manejar los mensajes
def reply(update, context):
  user_message = update.message.text
  response = get_response_from_huggingface(user_message)
  update.message.reply_text(response)

  # Configurar el bot
def main():
 updater = Updater(TELEGRAM_TOKEN, use_context=True)
 dp = updater.dispatcher

 dp.add_handler(CommandHandler("start", start))
 dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

 updater.start_polling()
 updater.idle()

 if __name__ == "__main__":
   main()

   # Iniciar el bot con polling
   print("Bot iniciado...")
   bot.infinity_polling()