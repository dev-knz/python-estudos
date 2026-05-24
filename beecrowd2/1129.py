# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())

entrada = input().split()
matriz = []

for i in range(n):
    matriz.append(int(entrada[i]))

fator = int(input())
quantidade = 0

for i in range(n):
    if matriz[i] == fator:
        quantidade += 1
        
