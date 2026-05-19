n = int(input())
m = int(input())

vetor = []
for i in range(m):
    resposta = int(input())

    if resposta <= n:
        vetor.append(resposta)

for i in range(len(vetor)):
    for j in range(len(vetor)):
        if i < len(vetor) and j < len(vetor):
            if vetor[i] == vetor[j] and j != i:
                vetor.pop(j)
                j = j - 1
print(n - len(vetor))