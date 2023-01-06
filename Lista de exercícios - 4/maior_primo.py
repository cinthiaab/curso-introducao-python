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


def maior_primo(x):
    primo = False
    if (x % 2 == 0 and x != 2):
        x = x-1

    while (primo == False):
        primo = ePrimo(x)
        if (primo == False):
            x = x-2

    return x
