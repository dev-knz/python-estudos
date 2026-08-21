# Criar classe Churrasco

class Churrasco:

    def __init__(self, titulo, qntd):
        self.titulo = titulo
        self.qntd = qntd

    def analisar(self):
        padrao = 0.4 # 400 gramas por pessoa
        preco = 82.4 # Preço da carne por kg

        # Pegando a quantidade necessaria de gramas de carne
        carne = padrao * self.qntd

        # Preco
        preco = preco * carne

        return f"Quantidade de carne necessária: {carne} ; Valor: R${preco:,.2f} ; Cada pessoa pagará: R${preco/self.qntd:,.2f} para participar"

c1 = Churrasco('Churrasco dos colegas', 15)
print(c1.analisar())
        
        