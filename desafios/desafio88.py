# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

import random

lista = []
n = int(input('Insira quantos jogos vão ser gerados para a MEGA SENA: '))

for i in range(0, n):
    num = random.sample(range(1,61), 6)
    lista.append(num)

for i in range(0, n):
    print(lista[i])



