# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())
cont, i, linha = 0, 1, 0

while cont != n:
    print(f'{i} ', end='')
    i += 1
    linha += 1

    if linha == 3:
        print('PUM')
        cont += 1
        linha = 0
        i += 1
        