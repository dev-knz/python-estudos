# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
m, n = 1, 1
cont = 0
while True:
    m, n = map(int, input().split())

    if m <= 0 or n <= 0:
        break
    if m > n:
        maior = m
        menor = n

    else:
        maior = n
        menor = m

    for i in range(menor, maior+1):
        print(f'{i} ',end='')
        cont += i
    
    print(f'Sum={cont}')
    cont = 0

