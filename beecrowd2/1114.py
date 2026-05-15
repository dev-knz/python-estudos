n = int(input())

lista = list()
for i in range(n):
    lista.append(int(input()))

for i in range(n-1, -1, -1):
    print(lista[i], end=' ')