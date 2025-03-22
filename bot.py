import telebot

TOKEN = "7807962142:AAE5dkfA8y7T5YylhUuNWZuI5lq2R0FpPAs"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(f"Mensaje recibido: {message.text}")  # Depuración
        bot.reply_to(message, "¡Hola! Soy tu bot de Telegram.")

        print("Bot iniciado...")
        bot.polling(none_stop=True, interval=0, timeout=20)