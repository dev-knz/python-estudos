# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

x = int(input())
y = int(input())

inicio = min(x, y)
fim = max(x, y)

soma = 0
for i in range(inicio, fim + 1):
    if i % 13 != 0:
        soma += i

print(soma)