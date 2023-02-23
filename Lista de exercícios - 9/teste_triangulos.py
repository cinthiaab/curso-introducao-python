import classe_triangulo
import pytest


class TestTriangulo:
    @pytest.mark.parametrize("a, b, c, tipo_do_triangulo", [
        (4, 4, 4, "equilátero"),
        (10, 20, 30, "escaleno"),
        (2, 5, 2, "isóceles"),
    ])
    def test_tipo_triangulo(self, a, b, c, tipo_do_triangulo):
        t = classe_triangulo.Triangulo(a, b, c)
        assert t.tipo_lado() == tipo_do_triangulo

    @pytest.mark.parametrize("a, b, c, perimetro", [
        (4, 4, 4, 12),
        (10, 20, 30, 60),
        (2, 5, 2, 9),
    ])
    def test_perimetro(self, a, b, c, perimetro):
        t = classe_triangulo.Triangulo(a, b, c)
        assert t.perimetro() == perimetro

    @pytest.mark.parametrize("a, b, c, retangulo", [
        (4, 4, 4, False),
        (3, 4, 5, True),
        (2, 5, 2, False),
    ])
    def test_retangulo(self, a, b, c, retangulo):
        t = classe_triangulo.Triangulo(a, b, c)
        assert t.retangulo() == retangulo

    @pytest.mark.parametrize("a1, b1, c1, a2, b2, c2, iguais", [
        (4, 4, 4, 3, 4, 5, False),
        (2, 5, 2, 4, 10, 1, False),
        (2, 3, 5, 4, 6, 10, True),
        (2, 2, 2, 2, 2, 2, True),
    ])
    def test_semelhantes(self, a1, b1, c1, a2, b2, c2, iguais):
        t1 = classe_triangulo.Triangulo(a1, b1, c1)
        t2 = classe_triangulo.Triangulo(a2, b2, c2)

        assert t1.semelhantes(t2) == iguais
