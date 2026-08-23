# Cafeteira

from abc import ABC, abstractmethod

class BebidaQuente(ABC):

    def __init__(self):
        super().__init__()

    def preparar(self):
        print(f'{self.ferver_agua()}\n{self.misturar()}\n{self.servir()}')

    def ferver_agua(self):
        return 'Coloque a água no fogo até chegar aos 100 graus'

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):

    def __init__(self):
        super().__init__()

    def misturar(self):
        return 'Coloque o pó de café e adicione a água quente'

    def servir(self):
        return 'Adicione o café em uma garrafa e sirva em xícaras'

class Cha(BebidaQuente):

    def __init__(self):
        super().__init__()

    def misturar(self):
        return 'Coloque o sache do cha na água quente'

    def servir(self):
        return 'Sirva o chá em canecas.'

class Leite(BebidaQuente):

    def __init__(self):
        super().__init__()

    def misturar(self):
        return 'Misture o leite sei lá'

    def servir(self):
        return 'Sirva o leite quente'

l = Leite()

l.preparar()