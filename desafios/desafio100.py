# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somarPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior

import random, time

def sorteia(lista):
    lista.append(random.sample(range(0,101), 5))
    print('Gerando a lista: ', end='')
    for i in range(0, 5):
        print(f'{lista[0][i]} ', end='')
        time.sleep(1)
    print()

def somarPar(lista):
    soma = 0
    for i in range(0, 5):
        if lista[0][i] % 2 == 0:
            soma = soma + lista[0][i]
    print(f'A soma dos valores pares é de {soma}')

lista = []
sorteia(lista)
somarPar(lista)


    


