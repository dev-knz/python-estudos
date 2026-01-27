# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

n1 = int(input('Insira o primeiro valor '))
n2 = int(input('Insira o segundo valor '))
n3 = int(input('Insira o terceiro valor '))

if (n1 + n2 > n3) and (n1 + n3 > n2) and (n3 + n2 > n1):
    print('Ele pode virar um triângulo')
else: 
    print('Ele não pode ser um triângulo.')