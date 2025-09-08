Ci= float(input("Ingresar capital inicial: "))
interes= float(input("Ingresar tasa de interes anual(%): "))
t= float(input("Ingrsar numero de periodos/años: "))
interes_decimal= interes/100
#Formula de interes simple
Cfs= Ci*(1+(interes_decimal*t))
#Formula interes compuesto
Cfc= Ci*(1+interes_decimal)**t
#Calcular y mostrar el capital final usando interés simple y compuesto
print("Capiyal final usando el interes simple es: ", Cfs )
print("Capital final usando el inters compuesto es: ", Cfc)