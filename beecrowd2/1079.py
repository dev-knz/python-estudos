# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

lista = input().split()
lista = list(lista)

for i in range(len(lista)):
    lista[i] = int(lista[i])

lista2 = list()
for i in range(len(lista) - 1, -1, -1):
    lista2.append(lista[i])
print(lista2)