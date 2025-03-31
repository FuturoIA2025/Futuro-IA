# Importamos las librerías necesarias
from transformers import AutoModel, AutoTokenizer
import torch

# Rutas de tus archivos de modelo (cambia estas rutas a las correctas en tu dispositivo)
model_paths = [
    "ruta/a/model-00001-of-00003.safetensors",
        "ruta/a/model-00002-of-00003.safetensors",
            "ruta/a/model-00003-of-00003.safetensors"
            ]

 # Intentamos cargar cada modelo
for path in model_paths:
                print(f"Intentando cargar el modelo desde {path}...")

 
 # Cargar modelo y tokenizer
model = AutoModel.from_pretrained(path)
tokenizer = AutoTokenizer.from_pretrained(path)

# Verificación de carga exitosa
print(f"Modelo cargado correctamente desde {path}")
                                                                    
# Probar la inferencia básica
input_text = "Hola, soy un modelo de prueba"
input_ids = tokenizer.encode(input_text, return_tensors="pt")
output = model(input_ids)

# Mostrar la salida del modelo
print(f"Salida del modelo para el texto '{input_text}': {output}\n")

# Capturamos cualquier error y lo mostramos
print(f"Error al cargar el modelo desde {path}: {e}\n")
