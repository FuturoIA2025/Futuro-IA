import telegram
from transformers import pipeline
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, HUGGINGFACE_TOKEN

# Inicializar el bot de Telegram y el pipeline de Hugging Face
bot = telegram.Bot(token=TELEGRAM_TOKEN)
generator = pipeline('text-generation', model="Mistralai/Mistral-7B", use_auth_token=HUGGINGFACE_TOKEN)

def send_message(message):
 """Enviar mensaje al chat de Telegram"""
 bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

def main():
 """Generar respuesta y enviar al chat"""
response = generator("Escribe algo que pueda entender el bot...", max_length=100)[0]['generated_text']
send_message(response)

if __name__ == '__main__':
     main()