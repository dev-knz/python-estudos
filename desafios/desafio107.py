# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções

from desafio107_moeda import metade, dobro, diminuir, aumentar

p = float(input('Digite o preço: '))
print(f'A metade de {p} é de: {metade(p)}')
print(f'O dobro de {p} é de: {dobro(p)}')
print(f'O valor aumentado de {p} é: {aumentar(p, 20)}')
print(f'O valor diminuido de {p} é: {diminuir(p , 20)}')
