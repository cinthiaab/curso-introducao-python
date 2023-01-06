def calculoDelta(a, b, c):
    return b**2 - 4*a*c


def deltaMaiorQueZero(a, b, delta):
    x = (-b + delta**(1/2))/2*a
    y = (-b - delta**(1/2))/2*a
    comparaXeY(x, y)


def comparaXeY(x, y):
    if (x == y):
        print("A raiz dupla desta equação é" + str(x))
    else:
        if (x < y):
            print("As raízes da equação são " + str(x) + " e " + str(y))
        else:
            print("As raízes da equação são " + str(y) + " e " + str(x))


def deltaIgualZero(a, b, delta):
    x = (-b + delta**(1/2))/2*a
    print("A raiz desta equação é " + str(x))


def deltaMenorQueZero():
    print("Esta equação não possui raízes reais")


def main():
    a = float(input("Insira o parametro a: "))
    b = float(input("Insira o parametro b: "))
    c = float(input("Insira o parametro c: "))
    delta = calculoDelta(a, b, c)
    imprimeRaizes(delta, a, b)


def imprimeRaizes(delta, a, b):
    if (delta > 0):
        deltaMaiorQueZero(a, b, delta)
    elif (delta == 0):
        deltaIgualZero(a, b, delta)
    else:
        deltaMenorQueZero()
