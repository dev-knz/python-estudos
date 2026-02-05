# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o menor e o maior peso lidos.

maior = 0
menor = 0
for i in range(0,5):
    n = int(input('Insira o seu peso '))

    if i == 0:
        if n > maior:
            maior = n
        if n > menor:
         menor = n
    else:
        if n > maior:
          maior = n
        if menor > n:
           menor = n
print('O maior número foi {}'.format(maior))
print('O menor número foi {}'.format(menor))