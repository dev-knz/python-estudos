# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())

horas = n // 3600

minutos = n // 60

while minutos >= 60:
    
    minutos = minutos - 60

segundos = n % 60 

print(f'{horas}:{minutos}:{segundos}')