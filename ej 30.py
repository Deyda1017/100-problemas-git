precio= float(input("Ingresar precion unitario: "))
cantidad= float(input("Ingresar cantidad vendida: "))
egresos= float(input("Ingresar egresos: "))
#Calcular ingreso total
ingresos= cantidad*precio
print("Ingreso total es igual a: ", ingresos)
ganancias= ingresos-egresos
print("Ganacias es: ", ganancias)
if ingresos-egresos:
    print("Hay perdidas")
elif ingresos==egresos:
    print("Punto de equilibrio")
else:
    print("Hay ganancias")