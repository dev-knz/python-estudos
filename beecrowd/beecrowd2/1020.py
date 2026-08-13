# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())

ano = n // 365
aux = n % 365

mes = aux // 30
aux = aux % 30

print(f'{ano} ano(s)\n{mes} mes(es)\n{aux} dia(s)')