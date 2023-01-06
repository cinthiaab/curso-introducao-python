def fatorial(x):
    resultado = 1
    while (x > 1):
        resultado = resultado * x
        x = x-1
    return resultado


def calculoCoeficienteBinomial(n, k):
    numBinomial = fatorial(n) / (fatorial(k)*fatorial(n-k))
    return numBinomial


def testarBinomial():
    if calculoCoeficienteBinomial(5, 3) == 10:
        print("A função está funcionado para n=5 e k=3")
    else:
        print("A função não está funcionado para n=5 e k=3")
    if calculoCoeficienteBinomial(10, 2) == 45:
        print("A função está funcionado para n=10 e k=2")
    else:
        print("A função não está funcionado para n=10 e k=2")
    if calculoCoeficienteBinomial(8, 7) == 8:
        print("A função está funcionado para n=8 e k=7")
    else:
        print("A função não está funcionado para n=8 e k=7")
    if calculoCoeficienteBinomial(9, 3) == 84:
        print("A função está funcionado para n=9 e k=3")
    else:
        print("A função não está funcionado para n=9 e k=3")
    if calculoCoeficienteBinomial(20, 12) == 125970:
        print("A função está funcionado para n=20 e k=12")
    else:
        print("A função não está funcionado para n=20 e k=12")


n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de k: "))

print(calculoCoeficienteBinomial(n, k))
testarBinomial()
