n, m = map(int, input().split())

tabela = []
for i in range(n):
    entrada = input().split()
    linha = []

    for j in range(m):
        linha.append(int(entrada[j]))

    tabela.append(linha)

qntd, contagem = int(input()), 0

for i in range(qntd):
        linha = list(map(int,input().split()))

        if linha[0] and linha[1] and tabela[linha[0] -1][linha[1] - 1]:
             tabela[linha[0]-1][linha[1]-1] -= 1
             contagem += 1

print(contagem)