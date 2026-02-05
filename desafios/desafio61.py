# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

p = int(input('Insira o primeiro termo da operação: '))
r = int(input('Insira a razão da PA: '))

while p < r*10+1:
    print(p)
    p = p+r