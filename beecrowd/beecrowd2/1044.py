# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

pos, par, neg, imp = 0, 0, 0, 0

for i in range(5):
    n = int(input())

    if n % 2 == 0:
        par += 1
        if n > 0:
            pos += 1
        if n < 0:
            neg += 1
    else:
        imp += 1
        if n > 0:
            pos += 1
        if n < 0:
            neg += 1

print(f'{par} valor(es) par(es)\n{imp} valor(es) impar(es)\n{pos} valor(es) positivo(s)\n{neg} valor(es) negativo(s)')
