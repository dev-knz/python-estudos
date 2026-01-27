# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km e R$0.45 para viagens mais longas.

n = int(input('Insira a distância de sua viagem '))

if n <= 200:
    preco = n*0.5
    print(f'O valor para a sua passagem será de R${preco:.2f}')
else:
    preco = n*0.45
    print(f'O valor para a sua passagem é de {preco:.2f}')