# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

cont = soma = 0
while True:
    n = int(input('Insira um valor:\nInsira [999] para finalizar o programa.  '))
    if n == 999:
        break
    cont += 1
    soma += n

print(f'Foram inseridos {cont} números')
print(f'A soma deles foi de {soma}')