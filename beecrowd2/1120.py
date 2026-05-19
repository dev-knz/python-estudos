# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

def bubble_sort(lista):
    trocou = True
    
    while trocou:
        trocou = False
        for i in range(len(lista) - 1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                trocou = True
    return lista
    
print(bubble_sort([4, 2, 7, 1, 3]))