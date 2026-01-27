# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

n = int(input('Insira um ano '))

if (n % 4 == 0) or (n % 400 == 0):
    print('Esse ano é bissexto')
else:
    print('Esse ano não é bissexto')