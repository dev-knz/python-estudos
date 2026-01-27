# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

n1 = random.randint(1,5)
n2 = int(input('Insira um valor de 1 a 5 '))

if n1 == n2:
    print('Parabéns, você escolheu o mesmo da máquina! ')
else:
    print('Puts, tente novamente. ')