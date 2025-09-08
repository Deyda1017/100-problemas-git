edad= float(input("Ingresar edad: "))
if(edad%1!=0):
    print("Edad invalida, vuelva a ingresar")
elif(edad<0 and edad>120):
    print("Edad invalida")
elif(edad<=10):
    print("Niño")
elif(edad>10 and edad<=17 ):
    print("Adolescente")
elif(edad>=18 and edad<=29):
    print("Joven")
elif(edad>=30 and edad<=59):
    print("Adulto")
else:
    print("Adultop mayor")