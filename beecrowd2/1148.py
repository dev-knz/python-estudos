def Le_lista():
    entrada = input().split()
    lista = []
    
    for i in range(len(entrada)):
        lista.append(int(entrada[i]))
    
    return lista

def Remove_Elementos(lista1, lista2):
    for i in range(len(lista2)):
        trocador = False
        for j in range(len(lista1)):
            if lista2[i] == lista1[j]:
                trocador = True
                aux = j
            
            if trocador and aux != j:
                troca = lista1[j]
                lista1[j-1] = troca
        lista1.pop()
    return lista1

def Imprime_lista(lista):
    for i in range(len(lista)):
        print(lista[i], end=' ')

n = int(input())

lista = Le_lista()
m = int(input())

lista2 = Le_lista()

lista = Remove_Elementos(lista, lista2)
Imprime_lista(lista)