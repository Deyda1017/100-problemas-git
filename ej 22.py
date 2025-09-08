num_preguntas= int(input("Ingresar numero de preguntas: "))
contestadas_correctamente= int(input("Cantidad de preguntas contestadas correctamentes son: "))
#Calcular calificacion en una escala del 0-10
calificacion= (contestadas_correctamente*10)/num_preguntas
print("Calificacion es: ", calificacion)