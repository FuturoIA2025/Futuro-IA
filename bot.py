import telebot

TOKEN = "7807962142:AAE5dkfA8y7T5YylhUuNWZuI5lq2R0FpPAs"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def responder_mensaje(message):
    bot.reply_to(message, f"Recibí tu mensaje: {message.text}")

    print("Bot funcionando...")
    bot.polling()