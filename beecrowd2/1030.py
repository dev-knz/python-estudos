# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

a, b = map(int, input().split())

if a > b and a % b == 0:
    print('Sao Multiplos')
elif b > a and b % a == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
