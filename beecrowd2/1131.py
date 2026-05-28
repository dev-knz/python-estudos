n, m = input().split()

n = int(n)
m = int(m)

matriz = []
soma = 0

for i in range(n):
    entrada = input().split()
    linha = []
    for i in range(m):
        linha.append(int(entrada[i]))
        soma = soma + linha[i]
    matriz.append(linha)
print(soma)