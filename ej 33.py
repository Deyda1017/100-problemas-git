nombre= input("Ingresar nombre: ")
ventas= float(input("Ingrese volumen de ventas en pesos: "))
if(ventas<1000):
   situacion= ("despedido")
elif(ventas>=1000 or ventas<=4999.99):
   situacion=("En perido de prueba")
elif(ventas>=5000 or  ventas<=9999.99):
   situacion=("Bono del 5%")
else:
   situacion=("Bono del 10%")
print(f"{nombre} : {situacion}")