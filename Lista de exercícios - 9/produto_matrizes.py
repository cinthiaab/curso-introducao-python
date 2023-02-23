import matriz_mult
import cria_matriz


def multiplicacao_matrizes(A, B):
    if (matriz_mult.sao_multiplicaveis(A, B) == True):
        linhas_matriz_A = len(A)
        linhas_matriz_B, colunas_matriz_B = len(B), len(B[0])

        matriz_final = cria_matriz.cria_matriz(
            linhas_matriz_A, colunas_matriz_B, 0)

        # Percorrendo a linha da matriz final
        for linha_matriz_A in range(linhas_matriz_A):
            # Percorrendo a coluna da matriz final
            for coluna_matriz_B in range(colunas_matriz_B):
                for coluna_do_A_linha_do_B in range(linhas_matriz_B):
                    matriz_final[linha_matriz_A][coluna_matriz_B] += A[linha_matriz_A][coluna_do_A_linha_do_B] * \
                        B[coluna_do_A_linha_do_B][coluna_matriz_B]  # Adicionando o produto dos elementos da matriz A e da matriz B

        return matriz_final
    else:
        print("Não é possível multiplicar essas matrizes.")


if __name__ == '__main__':
    A = [[2, 3], [1, 0], [4, 5]]
    B = [[3, 1], [2, 4]]
    print(multiplicacao_matrizes(A, B))
