def maiusculas(frase):
    letras_maiusculas = ''

    for letra in frase:
        if letra >= 'A' and letra <= 'Z':
            letras_maiusculas += letra

    return letras_maiusculas


def testa_maiusculas():
    if maiusculas('Programamos em python 2?') == 'P':
        print("Teste 1 funcionou.")
    else:
        print("Teste 1 não funcionou.")

    if maiusculas('Programamos em Python 3.') == 'PP':
        print("Teste 2 funcionou.")
    else:
        print("Teste 2 não funcionou.")

    if maiusculas('PrOgRaMaMoS em python!') == 'PORMMS':
        print("Teste 3 funcionou.")
    else:
        print("Teste 3 não funcionou.")
