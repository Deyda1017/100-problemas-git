import re
texto = input("Ingresa texto que contenga correos: ")
patron = r"([a-zA-Z0-9._%+-]+)@[a-zA-Z0-9.-]+\.[a-zA-Z]+"
usuarios = re.findall(patron, texto)
print("Usuarios encontrados:", usuarios)