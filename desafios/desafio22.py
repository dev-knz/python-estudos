# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letras ao todo (Sem considerar espaços)
# Quantas letras tem o primeiro nome

n = 'Lucifer dos Santos'
n1 = n.split()

print(f'Nome somente com caracteres maiúsculas: {n.upper()} ')
print(f'Nome com somente letras minúsculas: {n.lower()}')
print(f'Quantidade de caracteres sem espaços: {n.replace(' ','')}')
print(f'Caracteres do primeiro nome: {len(n1[0])}')

print(len(n))