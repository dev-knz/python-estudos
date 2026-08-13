# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


c1, n1, v1 = input().split()
c2, n2, v2 = input().split()

n1 = int(n1)
v1 = float(v1)
n2 = int(n2)
v2 = float(v2)

total = (n1 * v1) + (n2 * v2)

print(f'VALOR A PAGAR: R$ {total:.2f}')