# Escreva um programa que leia dois números, e veja qual deles é o maior.

n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))

if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n1 < n2:
    print(f'{n2} é maior que {n1}')
else:
    print('Os dois possuem o mesmo valor')