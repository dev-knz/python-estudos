# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

entrada = input().split()

l1 = list()
for i in range(len(entrada)):
    l1.append(int(entrada[i]))

entrada = input().split()

l2 = list()
for i in range(len(entrada)):
    l2.append(int(entrada[i]))

l3 = list()
for i in range(len(l1)):
    for n in range(len(l2)):
        if l1[i] == l2[n]:
            l3.append(l1[i])

print(l3)
