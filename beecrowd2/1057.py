# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

i, j = 1, 7
aux = 5

while True:
    print(f'I={i} J={j}')

    if i == 9 and j == 13:
        break

    if j == aux:
        i += 2
        j = aux + 4
        aux = j - 2
    else:
        j -= 1