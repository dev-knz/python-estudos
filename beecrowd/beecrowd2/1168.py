def Le_Lista(num):
    lista = []

    for i in range(num):
        lista.append(int(input()))
    return lista

def Inverte_Lista(lista):
    inicio, fim = 0, len(lista) - 1
    while inicio < fim:
        lista[inicio], lista[fim] = lista[fim], lista[inicio]
        inicio += 1
        fim -= 1
    return lista

def Imprime_Lista(lista):
    for i in range(len(lista)):
        print(lista[i], end=' ')

n = int(input())
lista = Le_Lista(n)
lista = Inverte_Lista(lista)
Imprime_Lista(lista)

