import random
import math


def lista_grande(n):
    if n >= 0:
        lista = []
        i = 0
        while (i < n):
            lista.append(math.ceil(10000000 * random.random()))
            i += 1
        return lista


def teste_lista_grande():
    print(lista_grande(70))
