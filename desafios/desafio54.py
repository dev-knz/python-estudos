# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores de 20 anos.

cont = 0
contn = 0

for i in range(1, 8):
    n = int(input('Insira o ano de nascimento: '))
    if 2026 - n > 19:
        cont += 1
    else:
        contn += 1
print(f'Existem {cont} pessoas de maioridade, e {contn} menores dessa idade')
