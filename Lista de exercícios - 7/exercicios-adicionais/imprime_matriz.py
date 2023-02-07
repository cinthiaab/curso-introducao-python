def imprime_matriz(matriz):
    for linha in matriz:
        num_colunas = len(linha)
        for index_coluna, elemento in enumerate(linha, start=1):
            if (index_coluna == num_colunas):
                print(elemento, end="")
            else:
                print(elemento, end=" ")
        print()
