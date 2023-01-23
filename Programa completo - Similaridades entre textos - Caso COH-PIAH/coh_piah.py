import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +
                  " (aperte enter para sair):").strip()
    while texto != "":
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +
                      " (aperte enter para sair):").strip()

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def calcular_tamanho_medio_palavras(texto):
    sentencas = separa_sentencas(texto)
    frases = []
    frase = []
    palavras = []
    palavra = []
    qtdeCaracteres = 0

    for i in range(len(sentencas)):
        frases.append(separa_frases(sentencas[i]))

    for sublist in frases:
        frase += sublist
    qtdeFrase = len(frase)

    for i in range(len(frase)):
        palavras.append(separa_palavras(frase[i]))

    for sublist in palavras:
        palavra += sublist

    for i in range(len(palavra)):
        qtdeCaracteres += len(palavra[i])

    media = qtdeCaracteres/len(palavra)

    return media


def calcularRTT(texto):
    sentencas = separa_sentencas(texto)
    frases = []
    frase = []
    palavras = []
    palavra = []
    qtdeCaracteres = 0

    for i in range(len(sentencas)):
        frases.append(separa_frases(sentencas[i]))

    for sublist in frases:
        frase += sublist
    qtdeFrase = len(frase)

    for i in range(len(frase)):
        palavras.append(separa_palavras(frase[i]))

    for sublist in palavras:
        palavra += sublist

    return n_palavras_diferentes(palavra) / len(palavra)


def calcularRHL(texto):
    sentencas = separa_sentencas(texto)
    frases = []
    frase = []
    palavras = []
    palavra = []
    qtdeCaracteres = 0

    for i in range(len(sentencas)):
        frases.append(separa_frases(sentencas[i]))

    for sublist in frases:
        frase += sublist
    qtdeFrase = len(frase)

    for i in range(len(frase)):
        palavras.append(separa_palavras(frase[i]))

    for sublist in palavras:
        palavra += sublist

    return n_palavras_unicas(palavra) / len(palavra)


def calcular_tamanho_medio_sentencas(texto):
    sentencas = separa_sentencas(texto)
    frases = []
    frase = []
    palavras = []
    palavra = []
    qtdeCaracteres = 0

    for i in range(len(sentencas)):
        frases.append(separa_frases(sentencas[i]))

    for sublist in frases:
        frase += sublist
    qtdeFrase = len(frase)

    for i in range(len(frase)):
        palavras.append(separa_palavras(frase[i]))

    for sublist in palavras:
        palavra += sublist

    for i in range(len(palavra)):
        qtdeCaracteres += len(palavra[i])

    qtdeCaracteres += len(palavra) + len(frase) - len(sentencas) - 1
    print(qtdeCaracteres / len(sentencas))

    return qtdeCaracteres / len(sentencas)


def calcular_complexidade_setencas(texto):
    sentencas = separa_sentencas(texto)
    frases = []
    soma = 0

    for i in range(len(sentencas)):
        frases.append(separa_frases(sentencas[i]))

    for i in range(len(sentencas)):
        soma = soma + len(frases[i])

    return soma / len(sentencas)


def calcular_tamanho_medio_frases(texto):
    sentencas = separa_sentencas(texto)
    frases = []
    frase = []
    palavras = []
    palavra = []
    qtdeCaracteres = 0

    for i in range(len(sentencas)):
        frases.append(separa_frases(sentencas[i]))

    for sublist in frases:
        frase += sublist
    qtdeFrase = len(frase)

    for i in range(len(frase)):
        palavras.append(separa_palavras(frase[i]))

    for sublist in palavras:
        palavra += sublist

    for i in range(len(palavra)):
        qtdeCaracteres += len(palavra[i])

    qtdeCaracteres += len(palavra) - 1

    return qtdeCaracteres / qtdeFrase


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma = 0
    i = 0
    while (i < 6):
        soma += abs(as_a[i] - as_b[i])
        i += 1

    return soma / 6


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    wal = calcular_tamanho_medio_palavras(texto)
    ttr = calcularRTT(texto)
    hlr = calcularRHL(texto)
    sal = calcular_tamanho_medio_sentencas(texto)
    sac = calcular_complexidade_setencas(texto)
    pal = calcular_tamanho_medio_frases(texto)

    return [wal, ttr, hlr, sal, sac, pal]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    similiaridade = []

    for i in range(0, len(textos)):
        similiaridade.append(compara_assinatura(
            calcula_assinatura(textos[i]), ass_cp))
    infectado = 1
    ass_cp = similiaridade[0]
    for i in range(1, len(similiaridade)):
        if (ass_cp > similiaridade[i]):
            ass_cp = similiaridade[i]
            infectado = i + 1

    return infectado


def main():
    assinaturaInfectado = le_assinatura()
    textos = le_textos()
    autorInfectado = avalia_textos(textos, assinaturaInfectado)
    print("O autor do texto", autorInfectado, "está infectado com COH-PIAH")


def testeCalcularAssinatura():
    texto = "Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova."

    resultadoObtido = calcula_assinatura(texto)
    print(resultadoObtido)

    resultadoEsperado = [4.507142857142857, 0.6928571428571428,
                         0.55, 70.81818181818181, 1.8181818181818181, 38.5]
    for i in range(len(resultadoEsperado)):
        if (resultadoEsperado[i] != resultadoObtido[i]):
            print("O teste de assinatura não funcionou")
        else:
            print("O teste de assinatura funcionou")
