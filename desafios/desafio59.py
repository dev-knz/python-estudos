# Crie um programa que leia dois valores e mostre um menu na tela:

n = 0
while n != 5:
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Menor\n[5] Sair do Programa')
    n = int(input('Insira a operação desejada: '))

    if n == 1:
        n1 = int(input('Insira um valor: '))
        n2 = int(input('Insira um valor: '))
        print(f'A soma desses valores é {n1+n2}')
    if n == 2:
        n1 = int(input('Insira um valor: '))
        n2 = int(input('Insira um valor: '))
        print(f'A multiplicação desses valores é {n1*n2}')
    if n == 3:
        n1 = int(input('Insira um valor: '))
        n2 = int(input('Insira um valor: '))
        if n1 > n2:
            print(f'{n1} é o maior dígito')
        elif n1 == n2:
            print('Possuem o mesmo valor')
        else:
            print(f'{n2} é o maior valor')
    if n == 4:
        n1 = int(input('Insira um valor: '))
        n2 = int(input('Insira um valor: '))
        if n1 < n2:
            print(f'{n1} é o menor valor')
        elif n1 == n2:
            print(f'São o mesmo valor')
        else:
            print(f'{n2} é o menor valor')
print('Fim')

        