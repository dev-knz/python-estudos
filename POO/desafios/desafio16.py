# Criar uma classe Funcionario

class Funcionario:

    empresa = 'Curso em Vídeo'

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return f"Funcionário: {self.nome} ; Setor: {self.setor} ; Cargo: {self.cargo} ; Empresa: {self.__class__.empresa}"

funcionario = Funcionario('Kevin', 'TI', 'Programador')
print(funcionario.apresentar())