def soma_matrizes(matriz1, matriz2):
    for linha_matriz1, linha_matriz2 in zip(matriz1, matriz2):
        coluna_matriz1 = len(linha_matriz1)
        coluna_matriz2 = len(linha_matriz2)
    if (len(matriz1) != len(matriz2) or coluna_matriz1 != coluna_matriz2):
        return False
    else:
        soma = []
        for linha_matriz1, linha_matriz2 in zip(matriz1, matriz2):
            soma_linha = []
            for elemento_matriz1, elemento_matriz2 in zip(linha_matriz1, linha_matriz2):
                soma_linha.append(elemento_matriz1+elemento_matriz2)
            soma.append(soma_linha)
        return soma
