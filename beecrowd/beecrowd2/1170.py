def Le_Lista():
    lista = []

    entrada = input().split()
    for i in range(len(entrada)):
        lista.append(int(entrada[i]))
    return lista

def Crescente(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] < lista[j] and i != j:
                lista[i], lista[j] = lista[j], lista[i]

    return lista

def Decrescente(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] > lista[j] and i != j:
                lista[i], lista[j] = lista[j], lista[i]
    return lista
 
