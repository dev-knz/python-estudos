# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108

from desafio107_moeda import metade, dobro, diminuir, aumentar, moeda

p = float(input('Digite o preço: '))
print(f'A metade de {moeda(p)} é de: {metade(p, escolha = True)}')
print(f'O dobro de {moeda(p)} é de: {dobro(p, escolha = True)}')
print(f'O valor aumentado de {p} é: {aumentar(p, 20, True)}')
print(f'O valor diminuido de {p} é: {diminuir(p , 20, True)}')