n = int(input())

matriz = []

for i in range(n):
    entrada = input().split()
    linha = []

    for i in range(n):
        linha.append(int(entrada[i]))
    matriz.append(linha)

soma_linha = []
for i in range(n):
    soma = 0
    for j in range(n):
        soma += matriz[i][j]
    soma_linha.append(soma)

soma_coluna = []
for j in range(n):
    soma = 0
    for i in range(n):
        soma += matriz[i][j]
    soma_coluna.append(soma)

maior = 0
for i in range(n):
    for j in range(n):
        peso = soma_linha[i] + soma_coluna[j] - 2*matriz[i][j]

        if peso > maior:
            maior = peso
print(maior)