# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:

# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

nome = None
gasto = produtos = 0
barato = 99999

while True:
    n = str(input('Insira o nome do produto: '))
    p = int(input('Insira o preço do produto: '))

    gasto += p
    if p > 1000:
        produtos += 1
    if barato > p:
        barato = p
        nome = n
    
    r = str(input('Deseja continuar? [S/N] '))
    if r == 'N':
        break
print(f'O produto mais barato é {nome}, custando {barato}')
print(f'O total gasto é de R${gasto}')
print(f'Existem {produtos} que custam mais caro de R$1000')
