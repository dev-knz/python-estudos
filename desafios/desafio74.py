# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

n1 = int(input('Insira um valor: '))
n2 = int(input('Insira um valor: '))
n3 = int(input('Insira um valor: '))
n4 = int(input('Insira um valor: '))
n5 = int(input('Insira um valor: '))

tupla = (n1, n2, n3, n4, n5)
print(tupla)

num = sorted(tupla)
print(f'O maior valor é {num[4]} e o menor é {num[0]}')