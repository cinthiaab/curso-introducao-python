def soma_lista(lista):
    if len(lista) > 1:
        lista[0] += lista.pop()
        return soma_lista(lista)
    elif len(lista) == 1:
        return lista[0]
    else:
        return 0
