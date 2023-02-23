class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b and self.b == self.c:
            tipo = "equilátero"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            tipo = "isóceles"
        else:
            tipo = "escaleno"

        return tipo

    def retangulo(self):
        if (self.c)**2 == (self.a)**2 + (self.b)**2:
            return True
        else:
            return False

    def __eq__(self, other):
        triangulo1 = self.a, self.b, self.c

        i = 0
        if isinstance(other, Triangulo):
            triangulo2 = other.a, other.b, other.c
            razao = []

            while (i < 3):
                razao.append(triangulo1[i]/triangulo2[i])
                i += 1

            i = 0
            while (i < 2):
                k = i + 1
                while (k < 3):
                    if razao[i] != razao[k]:
                        return False
                    k += 1
                i += 1
            return True
        else:
            False

    def semelhantes(self, other):
        if self == other:
            return True
        else:
            return False
