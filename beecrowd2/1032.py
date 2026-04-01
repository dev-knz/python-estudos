# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

inicio, fim = map(int, input().split())

if inicio == fim:
    hora = 24
elif inicio > fim:
    hora = abs(inicio - (fim+24))
else:
    hora = abs(fim - inicio)

print(f'O JOGO DUROU {hora} HORA(S)')
    