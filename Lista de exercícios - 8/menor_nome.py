def menor_nome(nomes):
    menor_tamanho = len(nomes[0])
    index_menor_nome = 0
    for index, nome in enumerate(nomes):
        tamanho = len(nome.strip())
        if tamanho < menor_tamanho:
            menor_tamanho = tamanho
            index_menor_nome = index

    return nomes[index_menor_nome].strip().title()


def testa_menor_nome():
    if menor_nome(['maria', 'josé', 'PAULO', 'Catarina']) == 'José':
        print("Teste 1 funcionou.")
    else:
        print("Teste não 1 funcionou.")

    if menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']) == 'José':
        print("Teste 2 funcionou.")
    else:
        print("Teste 2 não funcionou.")

    if menor_nome(['Bárbara', 'JOSÉ  ', 'Bill']) == 'José':
        print("Teste 3 funcionou.")
    else:
        print("Teste 3 não funcionou.")

    if menor_nome(['zé', ' lu', 'fê']) == 'Zé':
        print("Teste 4 funcionou.")
    else:
        print("Teste 4 não funcionou.")
