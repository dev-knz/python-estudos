lista = [1, 2, 3, 2, 4, 1, 5]

resultado = []

for i in range(len(lista)):
    repetido = False

    for j in range(i):
        if lista[i] == lista[j]:
            repetido = True

    if repetido == False:
        resultado.append(lista[i])

print(resultado)