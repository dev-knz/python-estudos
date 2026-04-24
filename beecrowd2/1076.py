# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

frase = str(input()).lower()

vogal, consoante = 0, 0

for letra in frase:
    if letra in 'aeiou':
        vogal += 1
    else:
        consoante += 1
print(f'Existem: {vogal} vogais')
print(f'Existem: {consoante} consoantes')