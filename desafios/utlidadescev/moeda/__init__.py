
def moeda(p = 0):
    return f'R${p:.2f}'.replace('.',',')


def metade(p = 0, escolha = False):
    valor = p / 2
    if escolha == True:
        return moeda(valor)
    else:
        return valor

def dobro(p = 0, escolha = False):
    valor = p * 2
    if escolha == True:
        return moeda(valor)
    else:
        return valor


def aumentar(p = 0, x = 0, escolha = False):
    x = (x / 100) + 1
    valor = p * x
    if escolha == True:
        return moeda(valor)
    else:
        return valor

def diminuir(p = 0, x = 0, escolha = False):
    valor = p - ((x/100) * p)
    if escolha == True:
        return moeda(valor)
    else:
        return valor


def resumo(p = 0, aumento = 0, diminui = 0):
    print('-'*30)
    print('         RESUMO DE VALOR  ')
    print('-'*30)


    print(f'Preço analisado: {moeda(p)}')
    print(f'Dobro do preço: {dobro(p, True)}')
    print(f'Metade do preço: {metade(p, True)}')

    if aumento != 0:
        print(f'{aumento}% de aumento: {aumentar(p, aumento, True)}')
    else:
        print(f'0% de aumento.')

    if diminui != 0:
        print(f'{diminui}% de diminuição: {diminuir(p, diminui, True)}')
    else:
        print(f'0% de diminuição')
    print('-'*30)