# Crie um programa que leia vários número inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer continuar ou não continuar a digitar valores.

soma = 0

media = 0
maior = 0
menor = 999

cont = 0
resp = 'SIM'

while resp == 'SIM':
    n = int(input('Insira um valor: '))
    soma = soma + n
    cont += 1
    
    if n > maior:
        maior = n
    elif menor > n:
        menor = n
    resp = input('DESEJA CONTINUAR? [SIM/NÃO]').upper()
media = soma / cont

print(f'A média é de {media}')
print(f'O maior número foi {maior}')
print(f'O menor número foi {menor}')


