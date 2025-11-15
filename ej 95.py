import requests
url = "https://api.open-meteo.com/v1/forecast?latitude=19.43&longitude=-99.13&current_weather=true"
respuesta = requests.get(url)
datos = respuesta.json()
clima = datos["current_weather"]
print("Temperatura actual:", clima["temperature"], "°C")
print("Velocidad del viento:", clima["windspeed"], "km/h")