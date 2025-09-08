cal= float(input("Ingresar calificacion: "))
if cal<0 or cal>0:
    print("Calificacion invalida")
elif cal<6:
    print("Es irregular")
elif cal>6 and cal<9.9:
    print("Es regular")
else:
    print("Es excelencia")