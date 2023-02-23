def cria_matriz(num_linhas, num_colunas, valor):
    matriz = []
    lin = 0

    while (lin < num_linhas):
        linha_da_matriz = []
        col = 0
        while (col < num_colunas):
            linha_da_matriz.append(valor)
            col += 1
        matriz.append(linha_da_matriz)
        lin += 1
    return matriz


if __name__ == '__main__':
    print(cria_matriz(3, 2, 15))
