# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido devidamente informado.

def ficha(nome, gols):
    if nome == '' and gols == '':
        nome = '<desconhecido>'
        gols = '0'
    elif nome == '':
        nome = '<desconhecido>'
    elif gols == '':
        gols = '0'

    print(f'O nome do jogador é {nome}')
    print(f'O número de gols desse jogador é de {gols}')


n = str(input('Insira o nome: '))
g = str(input('insira a quantidade de gols: '))


ficha(n, g)