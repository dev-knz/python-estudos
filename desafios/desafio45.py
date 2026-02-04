# Crie um programa que faça o computador jogar Jokenpô com você.

import random

n = input('Escolha entre [Pedra], [Papel] ou [Tesoura] ').upper()
r = ['PEDRA','PAPEL','TESOURA']
r = random.choice(r)

if n == 'PEDRA' and r == 'PAPEL':
    print(f'Você perdeu, você escolheu {n} e o bot {r}')
elif n == 'PAPEL' and r == 'PEDRA':
    print(f'Você ganhou, você escolheu {n} e o bot {r}')
elif n == 'TESOURA' and r == 'PAPEL':
    print(f'Você ganhou, você escolheu {n} e o bot {r}')
elif n == 'PAPEL' and r == 'TESOURA':
    print(f'Você perdeu, você escolheu {n} e o bot {r}')
elif n == 'PEDRA' and r =='TESOURA':
    print(f'Você ganhou, você escolheu {n} e o bot {r}')
elif n == 'TESOURA' and r == 'PEDRA':
    print(f'Você perdeu, você escolheu {n} e o bot {r}')
else:
    print(f'Empate! Você escolheu {n} e o bot {r}')