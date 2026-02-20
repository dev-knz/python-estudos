def contador(i, f, p):
    """
    --> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal CursoEmVideo
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('\nFim!')
 
help(contador)

# Parâmetro opcional
def somar(a, b, c = 0):
    s = a + b + c
    print(f'A soma vale {s}')


def subtrair(a, b = 0, c = 0):
    s = a - b - c
    return s

r = subtrair(1,2,3)
print(r)