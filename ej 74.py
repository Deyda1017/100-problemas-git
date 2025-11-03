import os
carpeta = input("Ingresa el nombre de la carpeta: ")

if os.path.isdir(carpeta):
    archivos = os.listdir(carpeta)
    csvs = sorted([f for f in archivos if f.endswith(".csv")])
    print("Archivos .csv encontrados:")
    for nombre in csvs:
        print("-", nombre)
else:
    print("La carpeta no existe")