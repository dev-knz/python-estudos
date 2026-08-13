# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())
aux = 0
print(n)

c100 = n // 100

aux = n % 100
c50 = aux // 50

aux = aux % 50
c20 = aux // 20

aux = aux % 20
c10 = aux // 10

aux = aux % 10
c5 = aux // 5

aux = aux % 5
c2 = aux // 2

aux = aux % 2
c1 = aux

print(f'{c100} nota(s) de R$ 100,00')
print(f'{c50} nota(s) de R$ 50,00')
print(f'{c20} nota(s) de R$ 20,00')
print(f'{c10} nota(s) de R$ 10,00')
print(f'{c5} nota(s) de R$ 5,00')
print(f'{c2} nota(s) de R$ 2,00')
print(f'{c1} nota(s) de R$ 1,00')


