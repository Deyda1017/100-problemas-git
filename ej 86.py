import re
correo = input("Ingresa un correo: ")
patron = r"^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+$"
if re.match(patron, correo):
    print("Válido")
else:
    print("Inválido")