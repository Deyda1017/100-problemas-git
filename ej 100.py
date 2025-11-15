import requests
url = "https://pokeapi.co/api/v2/pokemon?limit=5"
respuesta = requests.get(url)
datos = respuesta.json()
pokemon_lista = datos["results"]
print("Primeros 5 Pokémon:")
for p in pokemon_lista:
    print(p["name"])