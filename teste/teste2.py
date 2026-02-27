name = input('Insira o seu nome: ')
idade = int(input('Insira a sua idade: '))

print(f'Olá, {name}! Você tem {idade} anos.\nAno que vem você terá {idade + 1} anos.')


n = int(input('Insira a sua idade: '))

if n < 18:
    print('Você ainda é menor de idade.')
elif 18 <= n <= 59:
    print('Você é adulto.')
else:
    print('Você é experiente.')