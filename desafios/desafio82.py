# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdos das três listas.

resp = 'Y'
lista = []
par = []
impar = []

while resp == 'Y':
    n = int(input('Insira um valor: '))
    lista.append(n)

    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    
    resp = str(input('Deseja continuar? [Y/N]'))

print(f'A lista é: {lista}')
print(f'A lista somente com números pares é: {par}')
print(f'A lista somente com números ímpares é: {impar}')