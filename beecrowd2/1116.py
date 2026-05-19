entrada = input().split()

matriz = []
for i in range(len(entrada)):
    matriz.append(int(entrada[i]))

lista = []

seq = True
for i in range(len(matriz)):
    if i+1 < len(matriz):
        aux = abs(matriz[i] - matriz[i+1])
        lista.append(aux)
        
trocou = True
while trocou:
    trocou = False
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            trocou = True

for i in range(len(lista)):
    for j in range(len(lista)):
        if i < len(lista) and j < len(lista):
            if lista[i] == lista[j] and i != j:
                seq = False

if seq:
    print('C')
else:
    print('N')
