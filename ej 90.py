import re
texto = input("Ingresa un texto: ")
prohibidas = ["tonto", "feo", "bobo", "idiota"]
patron = r"(" + "|".join(prohibidas) + r")"
resultado = re.sub(patron, lambda m: "*" * len(m.group()), texto, flags=re.IGNORECASE)
print("Texto censurado:", resultado)