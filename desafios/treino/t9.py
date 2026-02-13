# Realizar um programa que leia um valor e exiba se ele é positivo ou negativo.

n = int(input('Insira um valor: '))

if n > 0:
    print('Esse valor é positivo')
elif n < 0:
    print('Esse valor é negativo')
else:
    print('Esse valor é nulo')