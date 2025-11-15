import requests
numero = input("Escribe un número: ")
url = f"https://numbersapi.com/{numero}?json"
respuesta = requests.get(url)
datos = respuesta.json()
print("Trivia:", datos["text"])