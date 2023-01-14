def proximoPrimo(num):
    primo = False

    while (primo == False):
        num = num + 1
        divisores = 0
        x = 1
        while (x < num and divisores <= 1):
            if (num % x == 0):
                divisores = divisores+1
            x = x + 1
        if (divisores == 1):
            primo = True
        else:
            primo = False

    return num


def main():
    num = int(input("Digite um número inteiro positivo: "))
    i = 2

    while (num != 1):
        multiplicidade = 0
        while (num % i == 0):
            num = num / i
            multiplicidade = multiplicidade + 1
        if (multiplicidade > 0):
            print("A múltiplicidade de", i, "é de", multiplicidade)
        i = proximoPrimo(i)
