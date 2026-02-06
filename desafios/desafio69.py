# Crie um programa que leia a idade o o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer continuar ou não continuar. No final, mostre: 

# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

adults = man = girl = 0
while True:
    i = int(input('Insira a idade: '))
    s = str(input('Insira se é homem ou mulher [H/M] '))

    if i > 18:
        adults += 1
    if s == 'H':
        man += 1
    if s == 'N' and i < 20:
        girl += 1
    
    r = str('Deseja continuar? [S/N] ')
    if r == 'N':
        break
print(f'Existem {adults} adultos')
print(f'Existem {man} homens')
print(f'Existem {girl} mulheres com menos de 20 anos.')