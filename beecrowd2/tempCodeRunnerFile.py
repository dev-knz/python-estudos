# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
lista = list()

n1, n2, n3 = map(int, input().split())

lista.append(n1)
lista.append(n2)
lista.append(n3)

lst = sorted(lista, reverse=True)
for i in lst:
    print(i)

print()
for i in lista:
    print(i)
