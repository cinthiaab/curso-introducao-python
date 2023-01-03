n = int(input("Digite o valor de n: "))

if (n >= 0):
    fatorial = 1
    while (n > 1):
        fatorial *= n
        n = n-1
    print(fatorial)
