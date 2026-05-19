# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

def soma_lista(number):
    soma = 0
    for i in range(len(number)):
        soma = soma + number[i]
    return soma

print(soma_lista([10,20,30]))