# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

x, y = map(int, input().split())

aux = 0
for i in range(1, y + 1):
    aux += 1

    if aux == x:
        print(f'{i}')
        aux = 0
    else:
        print(f'{i} ', end='')