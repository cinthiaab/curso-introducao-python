largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

i = 0
k = 0

while (i < altura):
    k = 0
    while (k < largura):
        print("#", end='')
        k = k + 1
    i = i + 1
    print()
