#Coordenadas del primer puto
x1= float(input("Ingrse x1: "))
y1= float(input("Ingrese y1: "))
#Cordenadas del segundo punto
x2= float(input("Ingrese x2: "))
y2= float(input("Ingrese y2: "))
if(x1==x2):
    print("La pendeintes es indefinida")
else:
    #Calcular la pendeinte
    m= (y2-y1)/(x2-x1)
    #Calcular la intersección con el eje Y (b)
    b = y1 - m * x1
print("La pendiente de la recta es: ", m)
#Formula deecuación en forma pendiente-intersección 
x= int
y= float(str((m*x) + b))
print("La ecuacion en forma pendiente-interseccion es: ")