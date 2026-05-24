# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
matriz = []
while True:
    resposta = int(input('-----MENU-----\n1) Adicionar\n2) Remover\n3) Listar\n4) Sair\n>- '))

    if resposta == 1:
        matriz.append(int(input('Insira o valor a ser adicionado na lista: ')))
    
    elif resposta == 2:
        indice = int(input('Insira a posição do indice do vetor a ser retirado: '))

        matriz.pop(indice)
    elif resposta == 3:
        print(matriz)

    else:
        break
