# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

import random

def maior(lista):
    m = 0

    for i in lista:
        if i > m:
            m = i
    print(f'\nO maior valor é {m}')

lst = random.sample(range(1,101), 5)
print('Gerando valores: ', end='')
for i in lst:
    print(f'{i} ',end='')

maior(lst)