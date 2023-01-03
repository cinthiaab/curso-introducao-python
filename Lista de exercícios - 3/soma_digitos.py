num = int(input("Digite um número inteiro: "))
soma = 0

while num // 10 != 0:
    soma = soma + (num % 10)
    num = num // 10
soma = soma + num
print(soma)
