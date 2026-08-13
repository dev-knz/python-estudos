# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

def maior_menor(lista):
    for i in range(len(lista)):
        if i == 0:
            maior, menor = lista[i], lista[i]
        
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
    return maior, menor
print(maior_menor([3, 1, 7, 2, 5]))
print(maior_menor([10, -2, 4]))