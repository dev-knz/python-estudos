# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem.

n1 = int(input('Insira o primeiro valor '))
n2 = int(input('Insira o segundo valor '))

if n1 > n2:
    print(f'O valor {n1} é maior do que {n2}')
elif n2 > n1:
    print(f'O valor {n2} é maior do que {n1}')
else:
    print('Os dois possuem o mesmo valor.')
    