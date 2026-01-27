# Faça um programa que leia três números e mostre qual é o maior e qual é o menor

n1 = int(input('Insira o primeiro valor '))
n2 = int(input('Insira o segundo valor '))
n3 = int(input('Insira o terceiro valor '))

n = [n1, n2, n3]
n.sort()
print(f'O valor mais baixo é: {n[0]}. O mais alto é: {n[2]}')