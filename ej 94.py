import requests
respuesta = requests.get("https://api.github.com")
print("Código de estado:", respuesta.status_code)
if respuesta.status_code == 200:
    print("Todo bien")
else:
    print("Algo salió mal")