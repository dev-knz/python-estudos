# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

def limpar():
    print('------------------------')

bd, sistem = [], {}
contagem, id = 0, 1

while True:
    limpar()
    num = int(input('1) Cadastrar\n2) Listar\n3) Sair\n> '))

    if num == 3:
        break
    
    if num == 1:
        sistem['id'] = id
        sistem['nome'] = str(input('Insira o nome do usuário: '))
        sistem['idade'] = int(input(f'Insira a idade do {sistem['nome']}: '))
        sistem['auxilio'] = str(input(f'[Y/N] para o auxílio: ')).upper()
        id += 1

        if sistem['auxilio'] == 'Y':
            sistem['salario'] = float(input('Insira o valor do auxílio: '))
        
        bd.append(sistem.copy())
        sistem.clear()
    
    else:
        for i in bd:
            print(f'Id: {i['id']}\nNome: {i['nome']}\nIdade: {i['idade']}\nAuxilio: {i['auxilio']}\nSalario: {i['salario']}\n')
    

