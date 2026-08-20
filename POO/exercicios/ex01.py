# Criando a primeira classe 
class MinhaClasse:
    """
Essa classe cria um MinhaClasse, que é uma pessoa com nome e idade.

Para criar uma nova pessoa, use:
variavel = MinhaClasse(nome, idade)

peps.python.org - site para melhorar as docs, mas por enquanto está otimo.
    """
    def __init__(self, nome = '', idade = 0): # Metodo construtor
        self.nome = nome
        self.idade = idade

    # Métodos de Instancia
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é gafanhoto e tem {self.idade} anos de idade."

    def __str__(self):
        # É possível alterar o docs padrao do print do objeto, caso default, ele retorna o endereço de memória da variável.
        return "Vou te mostrar alguma coisa quando usar o print"

    def __getstate__(self):
        return f"Estado: nome = {self.nome}"

# Instanciando objetos da minha classe
g1 = MinhaClasse("Kevin", 18)
g2 = MinhaClasse("Pablo", 20)
g3 = MinhaClasse("Maria", 18)

print(g1.mensagem())
print(g2.mensagem())
print(g3.mensagem())

# Exibe a documentação da classe - Dunder Atrribute
print(g1.__doc__)

# Exibe a mensagem padrão da função __str__, default = endereço de memória
print(g1)

# Exibe o dicionário da classe, os nomes dos parametros e valores atribuidos do objeto.
print(g1.__dict__) # Attributo
print(g1.__getstate__()) # Metodo, que é possível de ser alterado
