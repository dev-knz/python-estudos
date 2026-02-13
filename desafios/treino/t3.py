# Escreva um algoritmo que leia idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa em dias.

# Considerando ano 365 dias como um ano.   

a = int(input('Insira quantos anos você tem: '))
m = int(input('Insira quantos meses você tem: '))
d = int(input('Insira quantos dias você tem: '))

print(f'Você tem {(a*365)+(m*30)+d} dias de vida')