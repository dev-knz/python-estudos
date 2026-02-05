# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Insira um número: '))
cont = 0

for i in range(1, n+1):
    if n == 1 or n == 0:
        print('Este número não é primo')
        break
    else:
        primo = n % i
        if(primo == 0 and i != 1):
            cont += 1
if cont > 1:
    print('Este número não é primo. ')
else:
    print('Este número é primo!')
