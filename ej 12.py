#Recibir nombre y edad
print("Ingrese nombre")
nombre= input()
print("Ingrese edad")
edad= int(input())
#Saluda al usuario e indica su probable año de nacimiento
print("Hola", nombre, ",ingrese año actual")
año_actual= int(input())
print("Tu año de nacimiento es:", año_actual-edad)