# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

frase = str(input()).lower()
frase_final = ''

for let in frase:
    
    for i in range(len(alfabeto)):
        if alfabeto[i] == let:
            frase_final = frase_final + str(i)

print(frase_final)