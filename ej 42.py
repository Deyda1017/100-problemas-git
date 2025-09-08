contraseña= input("Ingrese contraseña:")
confirmacion= input("Confirme la contraseña: ")
intentos= 1
while contraseña!=confirmacion and intentos<3:
    print("Las  contraseñas no coinciden, intententelo de nuevo")
    contraseña= input("Ingrese contraseña:")
    confirmacion= input("Confirme la contraseña")
    intentos=intentos+1
if contraseña==confirmacion:
    print("Contraseña confrimada correctamente")
else:
    print("Cuenta cancelada")