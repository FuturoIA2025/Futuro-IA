from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Nombre del modelo
model_name = "mistralai/Mistral-7B"

# Cargar el modelo y el tokenizador
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")

# Prueba de generación de texto
input_text = "¿Qué es la inteligencia artificial?"
inputs = tokenizer(input_text, return_tensors="pt").to("cuda")

# Generar respuesta
output = model.generate(**inputs, max_length=100)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print("Respuesta:", generated_text)