def Le_lista():
    lista = []
    entrada = input().split()

    for i in range(len(entrada)):
        lista.append(int(entrada[i]))
    return lista

def Intersseccao_listas(l1, l2):
    l3 = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                l3.append(l1[i])
    return l3

def Imprime_lista(lista):
    for i in range(len(lista)):
        print(lista[i], end=' ')

n = int(input())
l1 = Le_lista()
l2 = Le_lista()
a = Intersseccao_listas(l1,l2)
Imprime_lista(a)