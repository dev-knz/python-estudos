def Le_lista():
    lista = []

    entrada = input().split()
    for i in range(len(entrada)):
        lista.append(int(entrada[i]))
    
    return lista

def Soma_pares(lista):
    soma = 0

    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            soma += lista[i]
    return soma

def Soma_impares(lista):
    soma = 0

    for i in range(len(lista)):
        if lista[i] % 2 != 0:
            soma += 1

    return soma

n = int(input())
a = Le_lista()

b = Soma_impares(a)
c = Soma_pares(a)

print(c, b)