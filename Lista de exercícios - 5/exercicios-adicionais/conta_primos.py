def ePrimo(num):
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

    return primo


def n_primos(n):
    x = 2
    qtde = 0
    if (n >= 2):
        while (x <= n):
            if (ePrimo(x)):
                qtde = qtde + 1
            x = x + 1
    return qtde
