n = int(input())

entrada = input().split()
vetor = []

for i in range(n):
    vetor.append(int(entrada[i]))

for i in range(len(vetor)):
    for j in range(len(vetor)):
        if i < len(vetor) and j < len(vetor):
            if vetor[i] == vetor[j] and i != j:
                vetor.pop(j)
                j = j - 1
print(len(vetor))