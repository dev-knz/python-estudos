# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

s = input('Insira o sexo: ').upper()

while s != 'M' and s != 'F':
    s = input('Valor inválido, tente novamente: ')
print('Fim')