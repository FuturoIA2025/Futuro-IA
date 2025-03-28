from dotenv import load_dotenv
import os
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
print("TELEGRAM_TOKEN:", TELEGRAM_TOKEN)
print("HUGGINGFACE_TOKEN:", HUGGINGFACE_TOKEN)