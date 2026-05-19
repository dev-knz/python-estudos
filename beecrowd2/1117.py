# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

def inverter(lista):
    inicio, fim = 0, len(lista) - 1
    
    while inicio > fim:
        lista[inicio], lista[fim] = lista[fim], lista[inicio]
        inicio += 1
        fim -= 1
    return lista

print(inverter([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))