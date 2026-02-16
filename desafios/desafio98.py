# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo e realize a contagem.

# Seu programa tem que realizar três contagens através da função criada:

# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio > fim:
        fim = fim - 1
    elif inicio < fim:
        fim = fim + 1

    for i in range(inicio, fim, passo):
        print(f'{i} ', end='')
    print()

contador(1,10, 1)
contador(10, 0, 2)

inicio = int(input('Insira o início da contagem: '))
fim = int(input('Insira o final da contagem: '))
passo = int(input('Insira o passo da contagem: '))

contador(inicio, fim, passo)