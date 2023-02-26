def ordena(lista):

    for i in range(len(lista)):
        menor = lista[i]
        indiceMenor = i
        for j in range(i+1, len(lista)):
            if menor > lista[j]:
                menor = lista[j]
                indiceMenor = j
        if indiceMenor != i:
            lista[i], lista[indiceMenor] = lista[indiceMenor], lista[i]

    return lista


def teste_ordenada():
    listas = [[1, 6, 7, 9, 15, 99],
              [-1, -6, -7, -9, -15, -99],
              [99, 15, 9, 7, 6, 10],
              [-500, 23, 56, 1, 2, 3, 50, 56, 23, 33]
              ]

    i = 0
    while (i < len(listas)):
        print(ordena(listas[i]))
        i += 1
