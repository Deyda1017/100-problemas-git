import requests
url = "https://api.dictionaryapi.dev/api/v2/entries/en/example"
respuesta = requests.get(url)
datos = respuesta.json()
# JSON → lista → diccionario → meanings → definitions
palabra = datos[0]["word"]
definicion = datos[0]["meanings"][0]["definitions"][0]["definition"]
print("Palabra:", palabra)
print("Definición principal:", definicion)