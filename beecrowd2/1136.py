def le_vetor():
    lista = list(map(int, input().split()))
    return lista

def posicao_menor(list):
    menor = list[0]
    for i in range(len(list)):
        if list[i] < menor:
            menor = list[i]
    return menor

def remove_elemento(list, posicao):
    list = list.pop(posicao)
    return list

def imprime_list(list):
    for i in range(len(list)):
        print(list[i], end=' ')

lista = le_vetor()
print(posicao_menor(lista))
remove_elemento(lista, 1)
imprime_list(list=lista)