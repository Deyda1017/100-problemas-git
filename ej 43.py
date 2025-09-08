suma=0
while suma<100000:
    abono=float(input("Cantidad a a abonar?: "))
    while abono<0:
        print("Error, vuelva a ingresar abono")
        abono= float(input("¿Cantidad a abonar?: "))
    suma=suma+abono
print("Ya se alcanzo los 100,000, Fin del programa") 
