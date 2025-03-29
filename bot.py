import telegram
from transformers import pipeline
from config import TELEGRAM_TOKEN, CHAT_ID, HUGGINGFACE_API_KEY

# Inicializar el bot de Telegram
bot = telegram.Bot(token=TELEGRAM_TOKEN)

# Crear el pipeline de Hugging Face
generator = pipeline('text-generation', model='gpt-2', api_key=HUGGINGFACE_API_KEY)

def send_message(message):
 """Enviar mensaje al chat de Telegram"""
 bot.send_message(chat_id=CHAT_ID, text=message)

 def generate_response(prompt):
    """Generar respuesta usando el modelo de Hugging Face"""
 response = generator(prompt, max_length=50, num_return_sequences=1)
 return response[0]['generated_text']

def main():
 """Función principal para manejar el flujo del bot"""
prompt = "Escribe algo que pueda entender el bot..."
response = generate_response(prompt)
send_message(response)

if __name__ == '__main__':
 main()