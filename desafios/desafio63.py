# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci.

n = int(input('Insira um número qualquer: '))

t1 = 0
t2 = 1
t3 = 0

cont = 3

print(f'{t1}')
print(f'{t2}')

while cont <= n:
    t3 = t1 + t2
    print(f'{t3}')
    t1 = t2
    t2 = t3
    cont += 1