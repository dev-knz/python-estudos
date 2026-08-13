# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

def inverte(lista):
    inicio, fim = 0, len(lista) - 1

    while inicio < fim:
        lista[inicio], lista[fim] = lista[fim], lista[inicio]

        inicio = inicio + 1
        fim -= 1
    return lista

print(inverte([1,2,3,4,5,6]))
