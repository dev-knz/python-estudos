# Criar a classe Gamer

class Gamer:

    def __init__(self, nome, nick, jogos = list()):
        self.nome = nome
        self.nick = nick
        self.jogos = jogos

    def add_favoritos(self, jogo):
        self.jogos.append(jogo)

    def imprimir(self):
        print(f"Usuario {self.nick} ; Nome: {self.nome}")
        print(f"Jogos favoritos do usuário:")

        for jogo in self.jogos:
            print(jogo)

g = Gamer('Kevin', 'Knz')
g.add_favoritos('God Of War')
g.add_favoritos('Pokemon')
g.imprimir()

