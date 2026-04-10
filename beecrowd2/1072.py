# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())

linha, aux, cont = 1, 1, 1

while cont != (n*2) + 1:

    if aux == 1:
        print(f'{linha**1} {linha**2} {linha**3}')
        aux += 1
    else:
        aux = 1
        print(f'{linha**1} {linha**2 + 1} {linha**3 + 1}')
        linha += 1
    cont += 1