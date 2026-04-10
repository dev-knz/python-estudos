# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

while True:
    n = int(input())

    if n:
        aux = 0
        for i in range(1, n+1):
            aux += 1

            if aux == n:
                print(f'{i}')
            else:
                print(f'{i} ',end='')
    else:
        break