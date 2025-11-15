import re
password = input("Ingresa una contraseña: ")
mayus = re.search(r"[A-Z]", password)
minus = re.search(r"[a-z]", password)
numero = re.search(r"[0-9]", password)
if len(password) >= 8 and mayus and minus and numero:
    print("Contraseña segura")
else:
    print("Insegura")
