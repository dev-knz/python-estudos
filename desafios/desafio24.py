# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'

n = input('Digite o nome da sua cidade ')

n = n.upper().split()

if n[0] == 'SANTO': 
    print('A sua cidade começa com SANTO')
else:
    print('Sua cidade não começa com SANTO')