import re
texto = input("Ingresa un texto con fechas: ")
patron = r"\b\d{2}/\d{2}/\d{4}\b"
fechas = re.findall(patron, texto)
print("Fechas encontradas:", fechas)