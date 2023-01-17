numeros = []

num = int(input("Digite um número inteiro: "))
while (num != 0):
    numeros.append(num)
    num = int(input("Digite um número inteiro: "))
i = -1
while (i >= -len(numeros)):
    print(numeros[i])
    i = i - 1
