respuesta= input("¿Desea hacer una operacion?(si/no): ")
while respuesta.lower()=="si":
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Exponente")
    print("6. Modulo (residuo)")
    opcion=int(input("Ingrese una opcion (1,6 ): "))
    if opcion not in range(1,7):
        print("Opcion invalida, intente de nuevo")
        continue
    repetir="si"
    while repetir.lower()=="si":
        a= float(input("Ingrese primer numero: "))
        b= float(input("Ingrese segundo numero: "))
        if opcion==1:
            print("suma es:",  a+b)
        elif opcion==2:
             print("Resta es: ", a-b)
        elif opcion==3:
            print("Multipllicacion es: ", a*b)
        elif opcion==4:
            if b==0:
                print("Vuelva invalido, no s epuede dividir entre 0")
            else:
                print("Division es:", a/b)
        elif opcion==5:
            print("Exponente es: ", a**b)
        elif opcion==6:
            print("Residio es: ", a%b)
        else:
            print("Salir de la calculadora")
        repetir= input("Desea repetir la operacion?(si/no): ")
    respuesta=input("¿Desea hacer otra operacion?(si/no): ")
print("Fin del programa")