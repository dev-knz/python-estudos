# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

while True:
    x, y = map(int, input().split())

    if x > y:
        print('Decrescente')
    elif x < y:
        print('Crescente')
    else:
        break