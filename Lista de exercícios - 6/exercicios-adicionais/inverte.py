def inverterSequencia(lista):
    fim = len(lista)/2
    i = 0
    while (i < fim):
        aux = lista[len(lista)-1-i]
        lista[len(lista)-1-i] = lista[i]
        lista[i] = aux
        i = i + 1


def main():
    sequencia = []
    numero = int(input("Digite um número: "))
    while (numero != 0):
        sequencia.append(numero)
        numero = int(input("Digite um número: "))

    inverterSequencia(sequencia)

    for numero in sequencia:
        print(numero)


main()
