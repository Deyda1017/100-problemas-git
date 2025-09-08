num= float(input("Ingresee un numero: "))
print("Numero al cuadrado es: ", num**2)
respuesta=  input("Desea ingresar otro numero?(si/no): ")
while respuesta=="si":
    num= float(input("Ingresee un numero: "))
    print("Numero al cuadrado es: ", num**2)
    respuesta=  input("Desea ingresar otro numero?(si/no): ")
print("Se termian el programa")