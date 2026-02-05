# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles, desconsiderando o flag.

stq = 0
cont = 0
n = int(input('Insira um dígito: '))

while n != 999:
    if(n != 999):
        stq = n + stq
        n = int(input('Insira um dígito: '))
        cont += 1
print(stq)
print(cont)