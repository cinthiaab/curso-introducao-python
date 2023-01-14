def é_hipotenusa(c):
    hip = False
    a = 1
    while (hip == False and a != c):
        b = 1
        while (b != c and hip == False):
            l1 = c*c
            l2 = a*a + b*b
            if (l1 == l2):
                hip = True
            b = b + 1
        a = a + 1
    return hip


def soma_hipotenusas(n):
    i = 1
    soma = 0
    while (i <= n):
        if (é_hipotenusa(i)):
            soma = soma + i
        i = i + 1
    return soma
