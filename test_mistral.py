from transformers import AutoModelForCausalLM, AutoTokenizer

# Cargar el modelo y el tokenizador
model_name = "mistralai/Mistral-7B-v0.1"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Prueba con un texto de ejemplo
input_text = "Tu mensaje aquí"
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(inputs['input_ids'])

print(tokenizer.decode(outputs[0], skip_special_tokens=True))