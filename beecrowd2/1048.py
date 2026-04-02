# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())
dentro, fora = 0, 0

for i in range(n):
    p = int(input())

    if 10 <= p <= 20:
        dentro += 1

    else:
        fora += 1
print(f'{dentro} in')
print(f'{fora} out')