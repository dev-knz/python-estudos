entrada = input().split()

matriz = []

for i in range(len(entrada)):
    matriz.append(int(entrada[i]))

resultados = []
for i in range(len(matriz)):
    if i + 1 < len(matriz):
        resultados.append(abs(matriz[i] - matriz[i+1]))

repetido = False
for i in range(len(resultados)):
    for j in range(len(resultados)):
        if i < len(resultados) and j < len(resultados):
            if resultados[i] == resultados[j] and j != i:
                repetido = True
                j = j - 1

if repetido:
    print('N')
else:
    print('H')
