def Le_lista():
    lista = []
    entrada = input().split()

    for i in range(len(entrada)):
        lista.append(int(entrada[i]))
    
    return lista

def Diferenca_listas(lista1, lista2):
    lista = []
    for i in range(len(lista1)):
        falso = False
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                falso = True
        if not falso:
            lista.append(lista1[i])
        
    return lista

def Imprime_lista(lista):
    for i in range(len(lista)):
        print(lista[i], end=' ')

n = int(input())
l1 = Le_lista()
l2 = Le_lista()

l3 = Diferenca_listas(l1, l2)
if l3:
    Imprime_lista(l3)

    