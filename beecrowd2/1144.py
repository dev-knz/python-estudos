def Le_Lista():
    entrada = input().split()
    lista = []
    for i in range(len(entrada)):
        lista.append(int(entrada[i]))
    
    return lista

def Verifica_Listas(lista1, lista2):
    lista = []
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                lista.append(lista1[i])
    return lista

def Imprime_Lista(lista):
    if not lista:
        print('N')
        return
    
    for i in range(len(lista)):
        print(f'{lista[i]}', end=' ')

n, m = input().split()

lista1 = Le_Lista() 
lista2 = Le_Lista()

lista = Verifica_Listas(lista1, lista2)
Imprime_Lista(lista)


