# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média.

pessoa = {}
grupo = []
media = cont = 0

while True:

    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo: [M/F] ')
    pessoa['idade'] = int(input('Idade: '))

    cont += 1
    media = media + pessoa['idade']

    grupo.append(pessoa.copy())
    pessoa.clear()

    resposta = str(input('Deseja continuar? [Y/N] '))
    if resposta != 'Y':
        break

media = media / cont

print('-='*15)
print(f'O grupo tem {cont} pessoas')
print(f'A média de idade é de {media:.2f} anos.')

print(f'As mulheres cadastradas foram: ', end='')
for i in grupo:
    if grupo['sexo'] == 'F':
        print(f'{grupo["nome"]} ')
print()

print('Lista das pessoas que estão acima da média: ', end='')
for i in grupo:
    if grupo['idade'] > media:
        print(f'{grupo["nome"][i]} ')
