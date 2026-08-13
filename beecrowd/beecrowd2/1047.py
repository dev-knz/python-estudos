# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

x = int(input())
y = int(input())

if x > y:
    maior = x
    menor = y
else:
    maior = y
    menor = x
soma = 0

for i in range(menor + 1, maior):
    if i % 2 != 0:
        soma += i

print(soma)