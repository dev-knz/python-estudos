from abc import ABC, abstractmethod

class Transporte(ABC):

    def __init__(self, distancia):
        self.distancia = distancia

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):

    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 0.5

    def calc_frete(self):
        return self.fator * self.distancia

class Caminhao(Transporte):

    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 1.2

    def calc_frete(self):
        if self.distancia < 50:
            return f'Esta encomenda não atende aos requisitos de frete do caminhão'

        return self.fator * self.distancia

class Drone(Transporte):

    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 9.5

    def calc_frete(self):
        if self.distancia > 10:
            return f'Esta encomenda não atende aos requisitos de frete do drone'

        return self.fator * self.distancia
       