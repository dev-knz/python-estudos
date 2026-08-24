from abc import ABC, abstractmethod

class Funcionario(ABC):

    def __init__(self, nome, sal_bruto = 0, salario = 0, sal_min = 1612, inss = 7.5):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario
        self.sal_min = sal_min
        self.inss = inss

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        return self.calc_sal() / self.sal_min

class Horista(Funcionario):

    def __init__(self, nome, valor_hora, horas_trabalhadas, sal_bruto=0, salario=0, sal_min=1612, inss=7.5):
        super().__init__(nome, sal_bruto, salario, sal_min, inss)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calc_sal(self):
        return (self.valor_hora * self.horas_trabalhadas) - (self.sal_bruto / self.inss)

class Mensalista(Funcionario):

    def __init__(self, nome, sal_bruto, salario = 0, sal_min=1612, inss=7.5):
        super().__init__(nome, sal_bruto, salario, sal_min, inss)

    def calc_sal(self):
        return self.sal_bruto - (self.sal_bruto / self.inss)