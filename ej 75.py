import sys

if len(sys.argv) != 3:
    print("Uso: python lector.py archivo.txt n")
else:
    archivo = sys.argv[1]
    try:
        n = int(sys.argv[2])
        with open(archivo, "r") as f:
            for i, linea in enumerate(f):
                if i < n:
                    print(linea.strip())
    except FileNotFoundError:
        print("El archivo no existe.")
    except ValueError:
        print("El segundo argumento debe ser un número entero.")
