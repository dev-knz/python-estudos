# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())

entrada = input().split()
matriz = []

soma = 0
for i in range(n):
    matriz.append(int(entrada[i]))
    soma = soma + matriz[i]

soma = soma / n

media = 0
for i in range(n):
    if matriz[i] > soma:
        media += 1
print(media)