import re
texto = input("Ingresa un párrafo: ")
oraciones = re.split(r"[.!?]", texto)
for oracion in oraciones:
    oracion = oracion.strip()
    if oracion:
        print(oracion)