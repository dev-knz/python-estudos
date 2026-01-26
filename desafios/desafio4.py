# Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ela.

valor = input('Digite algum valor ')

print('A variável desse valor é uma ' , type(valor))
print('É número? ' , valor.isnumeric())
print('É feito por somente letras? ' , valor.isalpha())
print('É decimal? ' , valor.isdecimal())
print('É feito por letra e número? ' , valor.isalnum())