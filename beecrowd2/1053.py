# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

aux, maior = 0, 0
for i in range(100):
    n = int(input())
    if n > maior:
        maior = n
        aux = i
print(maior)
print(aux+1)
    
        