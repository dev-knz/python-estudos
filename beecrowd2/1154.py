
s, t = map(int, input().split())

lista = []
for i in range(t):
    lista.append(list(map(int, input().split())))

n = int(input())

caminhos = []
contagem = 0

for i in range(n):
    caminhos.append(list(map(int, input().split())))
    
    verdade = True
    for j in range(len(caminhos[i])):
        if j + 1 < len(caminhos) - 1:
            if not (caminhos[i][j] and caminhos[i][j+1]) in lista:
                verdade = False
    
    if verdade:
        contagem += 1

print(contagem)
