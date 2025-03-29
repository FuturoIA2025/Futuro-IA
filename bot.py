import os
import telegram
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, HUGGINGFACE_TOKEN

# Inicializar el bot de Telegram
bot = telegram.Bot(token=TELEGRAM_TOKEN)

# Crear el pipeline de Hugging Face para generación de texto con Mistral-7B
model_name = "Mistralai/Mistral-7B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=HUGGINGFACE_TOKEN)
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

def send_message(message):
 """Enviar mensaje al chat de Telegram"""
bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
def generate_response(prompt):
    """Generar respuesta utilizando el modelo Mistral-7B"""
response = generator(prompt, max_length=100, num_return_sequences=1)
return response[0]['generated_text']
def main():
 """Función principal para manejar la lógica del bot"""
prompt = "Escribe algo que pueda " \
 "entender el bot..."
response = generate_response(prompt)
send_message(response)

if __name__ == '__main__':
    main()
