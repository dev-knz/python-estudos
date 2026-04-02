# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())

for i in range(n):
    n1, n2, n3 = map(float, input().split())

    media = (n1 * 2) + (n2 * 3) + (n3 * 5)
    media = media / 10

    print(f'{media:.1f}')