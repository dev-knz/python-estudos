# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

alcool, gasolina, diesel = 0, 0, 0

while True:
    resposta = int(input())

    if resposta == 1:
        alcool += 1

    elif resposta == 2:
        gasolina += 1
    
    elif resposta == 3:
        diesel += 1
    
    if resposta == 4:
        break

print(f'MUITO OBRIGADO\nAlcool: {alcool}\nGasolina: {gasolina}\nDiesel: {diesel}')