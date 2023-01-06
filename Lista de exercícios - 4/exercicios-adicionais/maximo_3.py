def maximo(x, y, z):
    if (x > y):
        if (x > z):
            maior = x
        else:
            maior = z
    else:
        if (y > z):
            maior = y
        else:
            maior = z
    return maior
