def insertion_sort(lista):
    fim = len(lista)

    for i in range(1, fim):
        k = i - 1
        while (k >= 0):
            if (lista[i] < lista[k]):
                lista[i], lista[k] = lista[k], lista[i]
                print(lista)
            k = k - 1
            i = i - 1

    return lista
