from dotenv import load_dotenv
import os
from transformers import AutoModelForCausalLM, AutoTokenizer

# Cargar el archivo .env
load_dotenv()

# Obtener el token desde las variables de entorno
huggingface_token = os.getenv("HUGGINGFACE_TOKEN")

# Verificar si el token se cargó correctamente
if not huggingface_token:
    print("Error: El token de Hugging Face no se cargó correctamente desde el archivo .env.")
else:
    print("Token cargado correctamente.")

    # Cargar el modelo y el tokenizador
    model_name = "mistralai/Mistral-7B-v0.1"
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Prueba con un texto de ejemplo
    input_text = "Tu mensaje aquí"
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(inputs['input_ids'])

    print(tokenizer.decode(outputs[0], skip_special_tokens=True))