def Le_Lista():
    lista = []
    entrada = input().split()
    for i in range(len(entrada)):
        lista.append(int(entrada[i]))
    
    return lista

def Remove_Elementos(l1, l2):
    for i in range(len(l2)):
        trocar = False
        for j in range(len(l1)):
            if l1[j] == l2[i]:
                trocar = True
                aux = j
            if trocar and j != aux:
                l1[j-1] = l1[j]
        l1.pop()
    return l1

def Imprime_lista(lista):
    for i in range(len(lista)):
        print(lista[i], end=' ')


    return l1
n = int(input())
l1 = Le_Lista()
remove = int(input())
l2 = Le_Lista()
a = Remove_Elementos(l1,l2)
Imprime_lista(a)
