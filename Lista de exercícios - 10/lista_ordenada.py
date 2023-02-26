def ordenada(lista):
    if len(lista) != 0:
        for indice, elemento in enumerate(lista, start=1):
            if indice != len(lista) and elemento > lista[indice]:
                return False

        return True


def teste_ordenada():
    listas = [[1, 6, 7, 9, 15, 99],
              [-1, -6, -7, -9, -15, -99],
              [99, 15, 9, 7, 6, 10],
              [-500, 23, 56, 1, 2, 3, 50, 56, 23, 33]
              ]
    resultados = [True, False, False, False]
    i = 0
    while (i < len(listas)):
        if ordenada(listas[i]) == resultados[i]:
            print("O teste " + str(i+1) + " deu certo!")
        else:
            print("O teste " + str(i+1) + " não deu certo!")
        i += 1
