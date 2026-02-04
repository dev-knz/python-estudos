# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade. Sistema de alistamento militar, o programa também deverá mostrar quantos anos falta ou que passou do prazo.

n = int(input('Insira o seu ano de nascimento '))
n = 2026 - n

if n == 18:
    print('Seu momento de alistar ao exército chegou.')
elif n < 18:
    n1 = 18 - n
    print(f'Ainda faltam {n1} anos para você servir.')
else:
    n1 = n - 18
    print(f'Você já está {n1} anos atrasado para servir, compareça ao posto militar imediatamente.')