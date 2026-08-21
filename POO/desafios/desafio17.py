# Criar a classe Produto

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        return f"Produto: {self.nome} ; Preço: R${self.preco:,.2f}"

produto = Produto('Peixe', 400)

print(produto.etiqueta())