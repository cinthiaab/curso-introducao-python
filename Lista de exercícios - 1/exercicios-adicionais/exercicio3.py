num = input("Digite um número inteiro:")

if len(num)>1:
   dezena = num[len(num)-2]
else:
    dezena = 0

print("O dígito das dezenas é", dezena)