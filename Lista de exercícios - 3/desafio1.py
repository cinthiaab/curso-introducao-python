num = int(input("Digite um numero inteiro grande: "))
soma = 0

while num // 10 != 0:
    soma = soma + (num % 10)
    num = num // 10
soma = soma + num
print("O resultado da soma e", soma)
