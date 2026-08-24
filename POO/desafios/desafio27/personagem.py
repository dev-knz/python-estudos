from abc import ABC, abstractmethod
from random import randint, randrange

class Personagem(ABC):

    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo: Personagem, forca):
        forca = randint(0, forca)

        self.receber_dano(forca)

        alvo.vida = alvo.vida - forca
        return f'{self.nome}({self.vida}) atacou {alvo.nome}({alvo.vida}) com um golpe de força {forca}'

    def receber_dano(self, dano):
        

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Soco', 'Golpe de Machado', 'Pulo Giratorio']

    def curar(self):
        pass

class Mago(Personagem):

    def __init__(self, nome, vida, golpes):
        super().__init__(nome, vida, golpes)
        self.golpes = ['Bola de fogo', 'Chuva ácida', 'Explosão galática']

    def curar(self):
        pass