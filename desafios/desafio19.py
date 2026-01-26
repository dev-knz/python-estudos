# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

n1 = input('Insira o nome do primeiro aluno ')
n2 = input('Insira o nome do segundo aluno ')
n3 = input('Insira o nome do terceiro aluno ')
n4 = input('Insira o nome do quarto aluno ')

n = [n1, n2, n3, n4]
print(f'O azarado foi o {random.choice(n)}')
