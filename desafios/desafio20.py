# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

n1 = input('Insira o nome do primeiro aluno ')
n2 = input('Insira o nome do segundo aluno ')
n3 = input('Insira o nome do terceiro aluno ')
n4 = input('Insira o nome do quarto aluno ')

lista = [n1, n2, n3, n4]
random.shuffle(lista)

print(f'A ordem para a apresentação é {lista}')