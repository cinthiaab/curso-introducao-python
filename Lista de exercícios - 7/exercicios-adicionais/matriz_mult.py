def sao_multiplicaveis(matriz1, matriz2):
    num_linhas_matriz2 = len(matriz2)
    for linha in matriz1:
        num_colunas_matriz1 = len(linha)

    if (num_linhas_matriz2 == num_colunas_matriz1):
        return True
    else:
        return False
