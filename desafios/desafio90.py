# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

boletim = {} # Definindo um dicionário

n = str(input('Nome: '))
media = float(input(f'Média de {n}: '))

boletim['nome'] = n
boletim['media'] = media

print(f'Nome é igual a {boletim['nome']}')
print(f'Média igual a {boletim['media']}')

if media >= 7:
    print('Situação é igual a Aprovado')
else:
    print('Situação é igual a Reprovado')