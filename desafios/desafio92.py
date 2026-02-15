# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar, sabendo que o funcionário deve contribuir com 35 anos.

from datetime import date

dic = {}
data = date.today().year

n = str(input('Nome: '))
dic['nome'] = n

ano = int(input('Ano de nascimento: '))

ano = data - ano
dic['idade'] = ano

ctps = int(input('Carteira de Trabalho: '))
if ctps != 0:
    dic['ctps'] = ctps
    ano = int(input('Ano de contratação: '))
    dic['contratação'] = ano
    salario = float(input('Salario: R$'))
    dic['salário'] = salario
    dic['aposentadoria'] = 35 - (data-ano) + dic['idade']

print(f'Nome da pessoa: {dic["nome"]}') 
print(f'Idade é igual a: {dic["idade"]}')

if ctps != 0:
    print(f'Carteira de trabalho igual a {dic["ctps"]}')
    print(f'Contratação de ano: {dic["contratação"]}')
    print(f'Salário de: {dic["salário"]}')
    print(f'Aposentadoria com: {dic["aposentadoria"]}')

