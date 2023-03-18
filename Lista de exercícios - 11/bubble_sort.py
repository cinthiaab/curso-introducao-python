def bubble_sort(lista):
    ListaOrdenada = False
    fim = len(lista)-1
    i = 0
    while (not ListaOrdenada):
        OcorreuTroca = False
        for i in range(fim):
            if lista[i+1] < lista[i]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                OcorreuTroca = True
                print(lista)
        if OcorreuTroca == False:
            ListaOrdenada = True

    return lista
