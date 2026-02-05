# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

# A média da idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos

media = 0
idadeV = 0
nomeV = None
mulher = 0

for c in range(1,5):
    n = input('Insira o nome: ')
    i = int(input('Insira a idade: '))
    s = input('Insira se é masculino ou feminino: ').upper().strip()

    media += i
    
    if s == 'FEMININO' and i < 21:
        mulher += 1
    if s == 'MASCULINO' and i > idadeV:
        idadeV = i
        nomeV = n

media = media / 4

print(f'A média de idade deles é de: {media}')
print(f'O nome do homem mais velho é: {nomeV} com {idadeV} anos')
print(f'Existem {mulher} mulheres menores ou com 20 anos')