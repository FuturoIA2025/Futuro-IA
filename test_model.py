 # Importamos las librerías necesarias
import torch
from safetensors import safe_open
from transformers import AutoModel, AutoTokenizer
# Rutas de tus archivos de modelo (cambia estas rutas a las correctas en tu dispositivo)
model_paths = [
     "ruta/a/model-00001-of-00003.safetensors",
         "ruta/a/model-00002-of-00003.safetensors",
             "ruta/a/model-00003-of-00003.safetensors"
             ]

 # Archivo de registro de errores
log_file = "errores_log.txt"

# Intentamos cargar cada modelo
for path in model_paths:
                 print(f"Intentando cargar el modelo desde {path}...")
 # Usamos safetensors para abrir el archivo y extraer los pesos
with safe_open(path, framework="pt") as f:
# Aquí puedes ajustar el nombre del tensor según tu modelo
                                                             model_weights = f.get_tensor("model")  # Obtén los pesos del modelo

                                                                     # Aquí es donde cargamos el modelo usando los pesos extraídos
                                                                             # Esto dependerá de la estructura de tu modelo, ajusta según sea necesario
                                                                                     # Por ejemplo, puedes usar el modelo de Hugging Face de esta manera:
                                                                                             
 # Usar AutoModel con los pesos
model_paths= AutoModel.from_pretrained('bert-base-uncased', state_dict=model_weights)  # Ajusta el modelo base según tu tipo
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')  # Asegúrate de usar el tokenizer correcto

# Verificación de carga exitosa
print(f"Modelo cargado correctamente desde {path}")
                                                                                                                                             
# Probar la inferencia básica
input_text = "Hola, soy un modelo de prueba"
input_ids = tokenizer.encode(input_text, return_tensors="pt")
output = model(input_ids)

# Mostrar la salida del modelo
print(f"Salida del modelo para el texto '{input_text}': {output}\n")

Exception 
# Capturamos el error y lo guardamos en el archivo de log
error_message = f"Error al cargar el modelo desde {path}: {e}\n"
print(error_message)  # También lo mostramos en la terminal para que lo veas rápidamente
                                                                                                                                                                                                                                 
# Escribir el error en el archivo de log
with open(log_file, "a") as file:
 file.write(error_message)
