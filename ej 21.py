nombre_evento= input("Imgresar noombre del evento: ")
fecha= input("Ingresar fecha del evento: ")
asistentes= int(input("Ingresar numero de asistentes: "))
#Cantidades por persona
agua_persona= float(1.5)
carne_persona= int(350)
salsa= agua_persona*0.25
#Calcular cantidad para el evento
agua_asistentes= agua_persona*asistentes
print("Cantidad de litros de agua de jamaica para el evento es: ", agua_asistentes)
carne_asistentes= carne_persona*asistentes
print("Cantidad de carne en gramos, para el evento es: ", carne_asistentes)
salsa_asistentes= salsa*asistentes
print("Cantida de litros de salsa para el evento es: ", salsa_asistentes)