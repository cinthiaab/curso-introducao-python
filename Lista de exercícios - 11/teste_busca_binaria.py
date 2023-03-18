import busca_binaria
import pytest


class TesteBuscaBinaria:
    @pytest.mark.parametrize("lista, elemento, retorno", [
        (['a', 'e', 'i'], 'e', 1),
        ([1, 2, 3, 4, 5], 6, False),
        ([1, 2, 3, 4, 5, 6], 4, 3),
    ])
    def test_busca_binaria(self, lista, elemento, retorno):
        assert busca_binaria.busca(lista=lista, elemento=elemento) == retorno

    def teste_busca():
        lista1 = [1, 2, 3, 4, 5]
        lista2 = [1, 2, 3, 4, 5, 6]
        elemento1 = 6
        elemento2 = 4

        busca_binaria.busca(lista=lista1, elemento=elemento1)
        print()
        busca_binaria.busca(lista=lista2, elemento=elemento2)


t = TesteBuscaBinaria
t.teste_busca()
