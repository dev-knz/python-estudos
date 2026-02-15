# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = []
par = []
impar = []

for i in range(0, 7):
    n = int(input(f'Digite o {i+1}o. valor: '))

    if n % 2 == 0:
        par.append(n)
    else: 
        impar.append(n)

lista.append(par[:])
lista.append(impar[:])

print(f'Os valores pares digitados foram: {sorted(lista[0])}')
print(f'Os valores ímpares digitados foram: {sorted(lista[1])}')