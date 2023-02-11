def remove_tudo_menos_letras(text):
    text = text.lower()
    return ''.join([letra for letra in text if letra.isalpha()])


def conta_letras(frase, contar="vogais"):
    frase = remove_tudo_menos_letras(frase)

    vogais = ['a', 'e', 'i', 'o', 'u']
    num_vogais = 0

    if contar == 'vogais':
        for vogal in vogais:
            num_vogais += frase.count(vogal)
        return num_vogais
    elif contar == 'consoantes':
        for vogal in vogais:
            num_vogais += frase.count(vogal)
        num_consoantes = len(frase) - num_vogais

        return num_consoantes


def testa_conta_letras():
    if conta_letras('programamos em python') == 6:
        print("Teste 1 funcionou.")
    else:
        print("Teste 1 não funcionou.")

    if conta_letras('programamos em python', 'vogais') == 6:
        print("Teste 2 funcionou.")
    else:
        print("Teste 2 não funcionou.")

    if conta_letras('programamos em python', 'consoantes') == 13:
        print("Teste 3 funcionou.")
    else:
        print("Teste 3 não funcionou.")
