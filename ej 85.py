import re
texto = input("Ingresa una cadena: ")
patron = r"\b[A-Z][a-zA-Z]*"
resultado = re.findall(patron, texto)
print("Palabras encontradas:", resultado)