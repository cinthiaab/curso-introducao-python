def busca(lista, elemento):
    elementoNaLista = False
    i = 0
    while (lista[i] != elemento and i < len(lista)-1 and elementoNaLista == False):
        i += 1

    if lista[i] == elemento:
        return i
    else:
        return elementoNaLista


def teste_busca():
    listas = [
        ['a', 'e', 'i'],
        [12, 13, 14],
        [1, 2, 3, -500, 100, 45]
    ]

    elementos = ['e', 15, 45]

    resultados = [1, False, 5]

    i = 0
    while (i < len(listas)):
        if busca(listas[i], elementos[i]) == resultados[i]:
            print("O teste " + str(i+1) + " deu certo!")
        else:
            print("O teste " + str(i+1) + " não deu certo!")
        i += 1
