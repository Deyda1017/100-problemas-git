print("Que desea calcular?")
print("1: si es el area")
print("2: si es el perimetro")
L= float(input("Ingresar lado: "))
if (L<=0):
    print("Error, debe ser numero positivo")
else:
    print("Lado es igual: ", L)
opcion= float(input("Ingresar 1 para area y 2 para perimetro: "))
if(opcion==1):
    a= L*L
    print("area es: ", a)
elif(opcion==2):
    p= L*4
    print("Perimetro es: ", p)
else:
    print("Error, debe ingresar 1 o 2")
