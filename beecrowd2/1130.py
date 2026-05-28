n = int(input())

matriz = []
for i in range(n):
    entrada = input().split()
    linha = []
    for i in range(n):
        linha.append(int(entrada[i]))
    matriz.append(linha)

for i in range(n):
    for j in range(n):
        if i >= j:
            print(matriz[i][j], end=' ')
    print()