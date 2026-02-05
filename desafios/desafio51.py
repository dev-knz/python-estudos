# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão

n = int(input('Insira um valor para o primeiro termo: '))
r = int(input('Insira o valor da razão da PA: '))

for i in range(n, r*10+1, r):
    print(i)

