# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())
divisao = 0

for i in range(n):
    x, y = map(int, input().split())
    
    if y:
        divisao = x / y
        print(f'{divisao:.1f}')
        
    else:
        print(f'divisao impossivel')
    