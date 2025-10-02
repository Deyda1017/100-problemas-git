def llenar_lista(n):
    lista = []
    for i in range(n):
        num = int(input(f"Ingrese el número {i+1}: "))
        lista.append(num)
    return lista
