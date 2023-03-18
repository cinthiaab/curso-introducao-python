import insertion_sort


class TesteInsertionSort:
    def teste_insert_sort():
        lista1 = [7, 3, 1, 2, 4, 6]
        lista2 = [2, 8, 5, 3, 9, 4]
        lista3 = [9, 13, 17, 19, 23, 84, 12]

        insertion_sort.insertion_sort(lista=lista1)
        print()
        insertion_sort.insertion_sort(lista=lista2)
        print()
        insertion_sort.insertion_sort(lista=lista3)


t = TesteInsertionSort
t.teste_insert_sort()
