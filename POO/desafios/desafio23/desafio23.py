# Poligono
# Neste caso, estou seguindo a risca o que foi pedido no exercício, assim, as funções retornam somente o valor
# Dando liberdade ao programador utilizar esses dados

from abc import ABC, abstractmethod

class Poligono(ABC):

    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):

    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado * self.lado

class Circulo(Poligono):

    def __init__(self, raio):
        super().__init__(0) 
        self.raio = raio

    def perimetro(self):
        return 2 * 3.14 * self.raio

    def area(self):
        return 3.14 * self.raio**2

q1 = Quadrado(8)

print(f'A área do quadrado é: {q1.area()}\nO perimetro do quadrado é: {q1.perimetro()}')

c1 = Circulo(10)

print(f'A área do círculo é: {c1.area()}\nO perimetro do círculo é: {c1.perimetro()}')