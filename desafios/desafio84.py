# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista = []
dados = []
maior = menor = 0
cont = 0
resposta = 'Y'

while resposta == 'Y':
    dados.append(str(input('Insira o nome: ')))
    dados.append(float(input('Insira o peso: ')))

    cont += 1
    if(cont == 1):
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    
    lista.append(dados[:]) # Copia a lista dados
    dados.clear() # Limpa a lista

    resposta = str(input('Deseja continuar? [Y/N] '))
    if resposta != 'Y':
        break

print(f'{cont} pessoas foram cadastradas ao sistema.')
print(lista)

print(f'O maior peso foi de {maior:.2f}Kg. Peso de ', end='')

for c in lista:
    if c[1] == maior:
        print(f'{c[0]} ', end='' )

print(f'\nO menor peso foi de {menor:.2f}Kg. Peso de ', end='')

for c in lista:
    if c[1] == menor:
        print(f'{c[0]} ', end='' )





