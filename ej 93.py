import requests
url = "https://numbersapi.com/42?json"
respuesta = requests.get(url)     # 1) Hacer petición GET
datos = respuesta.json()          # 2) Convertir a JSON
print("Trivia:", datos["text"])   # 3) Imprimir el campo 'text'