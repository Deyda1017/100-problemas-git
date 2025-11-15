import re
texto = input("Ingresa un texto: ")
patron = r"\b\d*\.\d+|\d+|\.\d+"
numeros = re.findall(patron, texto)
numeros_float = [float(n) for n in numeros]
print("Números encontrados:", numeros_float)