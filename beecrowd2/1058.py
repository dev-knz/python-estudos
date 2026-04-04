# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

i, j = 0, 1
x = 3
aux = 1

while True:
    print(f'I={i} J={i}')

    if j == x:
        i += 0.2
        j = aux + 0.2
        aux += 1
        x = 1
    else:
        j += 1
        x += 1
