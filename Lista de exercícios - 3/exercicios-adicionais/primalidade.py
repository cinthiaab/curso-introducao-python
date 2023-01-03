num = int(input("Digite um número inteiro: "))
primo = False
if (num % 2 != 0):
    x = 3
    while (x < num and primo == False):
        if (num % x):
            primo = True
            x = x+2
if (primo == False):
    print("não primo")
else:
    print("primo")
