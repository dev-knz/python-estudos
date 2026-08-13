# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())
cobaia, coelho, rato, sapo = 0, 0, 0, 0

for i in range(n):
    animais, codigo = input().split()

    animais = int(animais)

    if codigo == 'C':
        coelho += animais
    elif codigo == 'R':
        rato += animais
    else:
        sapo += animais
    cobaia += animais
     
print(f'Total: {cobaia} cobaias\nTotal de coelhos: {coelho}\nTotal de ratos: {rato}\nTotal de sapos: {sapo}\nPercentual de coelhos: {(coelho*100)/cobaia:.2f} %\nPercentual de ratos: {(rato*100)/cobaia:.2f} %\nPercentual de sapos: {(sapo*100)/cobaia:.2f} %')