# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

n = int(input('Insira o seu ano de nascimento: '))
n = 2026 - n

if n < 10:
    print('Você é MIRIM')
elif n < 15:
    print('Você é INFANTIL')
elif n < 20:
    print('Você é JUNIOR')
elif n < 21:
    print('Você é SÊNIOR')
else:
    print('Você é MASTER')