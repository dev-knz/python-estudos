def Le_lista():
    lista = []
    entrada = input().split()

    for i in range(len(entrada)):
        lista.append(int(entrada[i]))
    return lista

def Busca_Maiores(lista, x):
    valor, posicao = list(), list()
    for i in range(len(lista)):
        if lista[i] > x:
            valor.append(lista[i])
            posicao.append(i)
    if valor and posicao:
        return valor, posicao
    return False

def Imprime_lista(l1,l2):
    for i in range(len(l1)):
        print(l1[i], l2[i], end=' ')

n = int(input())
l1 = Le_lista()
x = int(input())
resposta = Busca_Maiores(l1, x)

if resposta:
    Imprime_lista(resposta[0], resposta[1])
else:
    print('N')
