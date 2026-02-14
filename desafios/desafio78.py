# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
for i in range(0, 5):
    n = int(input('Insira um valor: '))
    lista.append(n)

    if i == 0:
        maior = menor = n

    if n > maior:
        maior = n

    if n < menor:
        menor = n
        
print(f'A lista é {lista}')

print(f'O maior valor encontrado foi {maior} nas posições: ', end='')
for c, v in enumerate(lista):
    if v == maior:
        print(c , end=' ')

print(f'\nO menor valor encontrado foi {menor} nas posições: ', end='')
for c, v in enumerate(lista):
    if v == menor:
        print(c , end=' ')

 