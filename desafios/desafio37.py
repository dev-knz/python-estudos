# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão

# 1. para binário, 2. para octal e 3. para hexadecimal

n = int(input('Insira um valor: '))

print(f'O valor em binário será de {bin(n)}')
print(f'O valor em octal será de {oct(n)}')
print(f'O valor em hexadecimal será de {hex(n)}')