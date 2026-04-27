# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

entrada = input().split()
l = list()

for i in range(len(entrada)):
    l.append(int(entrada[i]))

i = 0
f = len(l) - 1
while i < f:
    aux = l[i]
    l[i] = l[f]
    l[f] = aux
    i += 1
    f -= 1
print(l)