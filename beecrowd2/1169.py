def Le_Lista():
    lista = []

    entrada = input().split()
    for i in range(len(entrada)):
        lista.append(int(entrada[i]))
    return lista

def Remove_Repetidos(lista):
    resposta = []
    
    for i in range(len(lista)):
        repetido = False
        for k in range(i):
            if lista[i] == lista[k]:
                repetido = True
        
        if not repetido:
            resposta.append(lista[i])
    return resposta

lista = Le_Lista()
lista = Remove_Repetidos(lista)

print(lista)