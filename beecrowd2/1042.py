# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

i, pos, cont = 0, 0, 0

while i != 6:
    n = float(input())

    if n > 0:
        pos += 1
        cont = cont + n

    i += 1

cont = cont / pos
print(f'{pos} valores positivos')
print(f'{cont:.1f}')