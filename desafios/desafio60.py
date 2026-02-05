# Faça um programa que leia um número qualquer e mostre o seu fatorial

n = int(input('Insira um valor: '))
res = 1

while n != 0:
    res *= n
    n = n - 1
print(res)
