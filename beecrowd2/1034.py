# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = float(input())

if 400 >= n >= 0:
    novo = n * 1.15
    ganho = n * 0.15
    reajuste = 15
elif 800 >= n >= 400.01:
    novo = n * 1.12
    ganho = n * 0.12
    reajuste = 12
elif 1200 >= n >= 800.01:
    novo = n * 1.10
    ganho = n * 0.10
    reajuste = 10
elif 2000 >= n >= 1200.1:
    novo = n * 1.07
    ganho = n * 0.07
    reajuste = 7
else:
    novo = n * 1.04
    ganho = n * 0.04
    reajuste = 4

print(f'Novo salario: {novo:.2f}\nReajuste ganho: {ganho:.2f}\nEm percentual: {reajuste} %')