def remove_repetidos(lista):
    lista.sort()
    i = 0
    while (i < len(lista)-1):
        if (i+1 in range(len(lista))):
            while (lista[i] == lista[i+1]):
                del lista[i+1]
        i = i + 1
    return lista
