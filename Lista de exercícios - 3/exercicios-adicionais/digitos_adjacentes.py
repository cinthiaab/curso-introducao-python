num = int(input("Digite um número inteiro: "))
adjacentes = False
digito = num % 10

while num // 10 != 0 and not adjacentes:
    anterior = digito
    num = num // 10
    digito = num % 10
    if (digito == anterior):
        adjacentes = True

if (adjacentes == True):
    print("sim")
else:
    print("não")
