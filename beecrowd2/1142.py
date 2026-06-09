def Le_lista():
    lista = []
    
    entrada = input().split()
    for i in range(len(entrada)):
        lista.append(int(entrada[i]))
    return lista

def Verifica_Faltantes(lista, n):
    contagem = 0
    achou = False

    for i in range(1, n+1):
        for j in range(len(lista)):
            if i == lista[j]:
                achou = True
        if not achou:
            contagem += 1
        achou = False
    return contagem

num = int(input())
tamanho = int(input())

figurinhas = Le_lista()
print(Verifica_Faltantes(figurinhas, num))
    

