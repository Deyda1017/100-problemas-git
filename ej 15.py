#Recibir nombre de un productoy su precio sin IVA
print("Ingresar nombre del producto")
producto= input()
print("Ingresar su precio sin IVA")
precio_producto= float(input())
#Calcular precio del producto con IVA
Precio_final= float(precio_producto*1.16)
print("Precio del producto con IVA es:", Precio_final)