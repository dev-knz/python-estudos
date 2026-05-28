n = int(input())

matriz = []

for i in range(n):
    entrada = input().split()
    linha = []
    for i in range(n):
        linha.append(int(entrada[i]))
    matriz.append(linha)

magico = True

soma = 0
for i in range(n):
    soma = soma + matriz[i][i]

compara = 0
for i in range(n-1, -1, -1):
    compara = compara + matriz[i][i]

if compara != soma:
    magico = False

compara = 0
if magico:
    for i in range(n):
        for j in range(n):
            compara = compara + matriz[i][j]
        if compara != soma:
            magico = False
        compara = 0
    
    for i in range(n):
        for j in range(n):
            compara = compara + matriz[j][i]
        if compara != soma:
            magico = False
        compara = 0

if magico:
    print(soma)
else:
    print(-1)


