class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)

        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        pass

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)

        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        pass

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)

        self.cargo = cargo
        self.setor = setor

        def bater_ponto(self):
            pass

# Nome e idade vieram da classe Pessoa.
a1 = Aluno("José", 17, "Informática", 'T01')
print(a1.__dict__)

p1 = Professor("Samuel", 37, "Biologia", "Doutorado")
print(p1.__dict__)

f1 = Funcionario("Kevin", 18, "Junior", "Informatica")
print(f1.__dict__)