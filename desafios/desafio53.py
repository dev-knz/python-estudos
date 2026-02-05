# Crie um programa que leia uma frase qualquer e diga se ela é palíndromo, desconsiderando os espaços

n = input('Insira uma frase ou nome: ').strip().upper()
n = n.replace(' ','')

m = n[::-1]

if n == m:
    print('É palíndromo.')
else:
    print('Não é.')

