# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
def contar(lista, fator):
    contagem = 0

    for i in range(len(lista)):
        if lista[i] == fator:
            contagem += 1
    return contagem

print(contar(['a', 'b', 'a'], 'a'))

