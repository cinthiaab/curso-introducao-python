def fatorial(n, fat=1):
    if n > 0:
        fat *= n
        return fat * fatorial(n-1)
    elif n == 0:
        return 1
    else:
        return fat
