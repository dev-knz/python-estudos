# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem de zero a vinte de modo extenso. Seu programa deverá ler um número e exibir ele em extenso.

e = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    n = int(input(('Insira um número de 0 a 20: ')))
    if n > 20 or n < 0:
        print('Número inválido, tente novamente.')
    else:
        print(e[n])
        break