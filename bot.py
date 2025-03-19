from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "7807962142:AAE5dkfA8y7T5YylhUuNWZuI5lq2R0FpPAs"  # Reemplaza con tu token de BotFather

# Función para responder al comando /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("¡Hola! Soy tu bot de Telegram.")

    # Función para responder a cualquier mensaje de texto
    async def responder(update: Update, context: CallbackContext):
        mensaje_usuario = update.message.text
            await update.message.reply_text(f"Recibí tu mensaje: {mensaje_usuario}")

            # Configurar el bot
            def main():
                app = ApplicationBuilder().token(TOKEN).build()

                    app.add_handler(CommandHandler("start", start))
                        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

                            print("El bot ha iniciado correctamente.")
                                app.run_polling()

                                if __name__ == "__main__":
                                    main()