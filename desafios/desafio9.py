# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

n = int(input('Digite um valor '))

for i in range(11):
    print('{} * {} = {}'.format(n,i,n*i))
