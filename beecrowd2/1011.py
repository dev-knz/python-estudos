# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

A, B, C = input().split()
pi = 3.14159

A = float(A)
B = float(B)
C = float(C)

TRIANGULO = (A*C)/2
CIRCULO = pi * C**2
TRAPEZIO = (A + B) * C / 2
QUADRADO = B*B
RETANGULO = A * B

print(f'TRIANGULO: {TRIANGULO:.3f}')
print(f'CIRCULO: {CIRCULO:.3f}')
print(f'TRAPEZIO: {TRAPEZIO:.3f}')
print(f'QUADRADO: {QUADRADO:.3f}')
print(f'RETANGULO: {RETANGULO:.3f}')

