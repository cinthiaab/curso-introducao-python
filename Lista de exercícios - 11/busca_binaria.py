def busca(lista, elemento):
    elementoEstaNaLista = False
    inicio = 0
    fim = len(lista) - 1

    while (inicio <= fim and not elementoEstaNaLista):
        meio = (inicio + fim)//2
        print(meio)
        if lista[meio] == elemento:
            elementoEstaNaLista = True
        elif lista[meio] > elemento:
            fim = meio - 1
        else:
            inicio = meio + 1

    if elementoEstaNaLista:
        resultado = meio
    else:
        resultado = False

    return resultado
