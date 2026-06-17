def Le_Lista():
    lista = []
    entrada = input().split()

    for i in range(len(entrada)):
        lista.append(int(entrada[i]))
    return lista

def Calcula_Caravanas(lista):
    resultado = []

    for i in range(len(lista)):
        repetido = False

        for j in range(i):
            if lista[i] == lista[j]:
                repetido = True

        if not repetido:
            resultado.append(lista[i])
    return len(resultado)

n = int(input())
lista = Le_Lista()
print(Calcula_Caravanas(lista))

