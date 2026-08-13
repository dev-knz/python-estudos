# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

def rotacionar(lista, fat):
    lista_aux = list()
    for i in range(fat + 1, len(lista)):
        lista_aux.append(lista[i])
    
    for i in range(0, fat + 1):
        lista_aux.append(lista[i])
    return lista_aux
print(rotacionar([1,2,3,4,5], 2))
print(rotacionar([1,2,3], 1))
        