# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

media = 0
validacao = 0

while validacao != 2:
    n = float(input())

    if n >= 0 and n <= 10:
        validacao += 1

        media += n 

    else:
        print('nota invalida') 

media = media / 2
print(f'media = {media:.2f}')