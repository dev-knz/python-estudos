# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições

import datetime

def voto(num):
    data = datetime.date.today()
    ano = data.year

    v = ano - num
    if v >= 18 and v < 65:
        print('O voto é OBRIGATÓRIO')
    elif v < 18:
        print('O voto é NEGADO')
    else:
        print('O voto é OPCIONAL')


voto(2008)
