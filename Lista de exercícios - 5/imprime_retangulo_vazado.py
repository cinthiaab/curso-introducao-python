largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

i = 0
k = 0

while (i < altura):
    k = 0
    while (k < largura):
        if ((k == 0 or k == largura-1) or (i == 0 or i == altura-1)):
            print("#", end='')
        else:
            print(end=' ')
        k = k + 1
    i = i + 1
    print()
