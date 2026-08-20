# Anotações baseado no Curso em Vídeo - Mundo 4 - Python

# POO = Programação Orientada a Objetos or OOP
# O objetivo da POO é representar elementos do mundo real nos sistemas computacionais.

# Classes, objetos, atributos e metodos - UML

# Declaração de classe
class MinhaClasse:
    def __init__(self): # Metodo construtor
        self.nome = ''
        self.idade = 0

    # Métodos de Instancia
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é gafanhoto e tem {self.idade} anos de idade."

# Definindo um objeto

obj = MinhaClasse()

obj.nome = "Kevin"
obj.idade = 18

print(obj.mensagem())
