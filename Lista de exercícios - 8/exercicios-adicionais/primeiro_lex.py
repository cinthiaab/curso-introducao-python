def primeiro_lex(lista):
    menor_lex = lista[0]
    for string in lista:
        if string < menor_lex:
            menor_lex = string

    return menor_lex


def testa_primeiro_lex():
    if primeiro_lex(['oĺá', 'A', 'a', 'casa']) == 'A':
        print("Teste 1 funcionou.")
    else:
        print("Teste 1 não funcionou.")

    if primeiro_lex(['AAAAAA', 'b']) == 'AAAAAA':
        print("Teste 2 funcionou.")
    else:
        print("Teste 2 não funcionou.")
