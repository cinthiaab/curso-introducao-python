def encontra_impares(lista):
    if len(lista) == 0:
        return []
    elif lista[0] % 2 != 0:
        return [lista[0]] + encontra_impares(lista[1:])
    else:
        return encontra_impares(lista[1:])
    lista_impares = [lista[0]] + encontra_impares(lista[1:])
    return lista_impares
