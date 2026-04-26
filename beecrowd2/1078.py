# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

# Sistema de cadastro

sistema, aluno = list(), dict()

while True:
    resposta = int(input('1) Cadastrar Aluno\n2) Listar Aluno\n3) Sair\n>'))

    if resposta == 3:
        break

    if resposta == 1:
        aluno['nome'] = str(input('Insira o seu nome: '))
        aluno['media'] = int(input('Insira a média do aluno: '))
        aluno['genero'] = str(input('[M/Y]: '))
        sistema.append(aluno.copy())
        aluno.clear()    
    if resposta == 2:
        print(sistema)  
        