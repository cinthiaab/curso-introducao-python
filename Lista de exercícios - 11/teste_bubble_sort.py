import bubble_sort


class TesteBubbleSort:
    def test_bubble_sort():
        lista = [5, 1, 4, 2]
        bubble_sort.bubble_sort(lista=lista)


t = TesteBubbleSort
t.test_bubble_sort()
