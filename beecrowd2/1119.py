# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

def remover_duplicadas(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if i < len(lista) and j < len(lista):
                if lista[i] == lista[j] and i != j:
                    lista.pop(j)
                    j = j - 1
    return lista
print(remover_duplicadas([1, 2, 2, 3, 1]))