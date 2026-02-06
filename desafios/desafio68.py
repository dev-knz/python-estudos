# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

cont = 0

while True:
    n1 = int(input('Insira um valor: '))
    n2 = random.randint(0,10)

    e = str(input('Insira se quer Par ou Ímpar [P/I] '))
    soma = n1 + n2

    if soma % 2 == 0 and e == 'P':
        print(f'Você venceu!\nA soma foi de {soma}')
        cont += 1
    elif soma % 2 != 0 and e == 'I':
        print(f'Você venceu!\nA soma foi de {soma}')
        cont += 1
    else:
        print(f'Você perdeu, a soma foi de {soma}')
        break
if cont == 0:
    print('Você não ganhou nenhuma partida')
else:
    print(f'Você venceu {cont} vezes seguidas! Orgulhe-se!')