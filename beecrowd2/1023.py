# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from math import sqrt
a, b, c = map(float, input().split())

bhaskara = (b**2) - 4*a*c


if a != 0 and bhaskara >= 0:
    bhaskara = sqrt(bhaskara)
    r1 = (-1 * b - bhaskara) / (2 * a)
    r2 = (-1 * b + bhaskara) / (2 * a)
    print(f'R1 = {r2:.5f}')
    print(f'R2 = {r1:.5f}')
else:
    print('Impossivel calcular')