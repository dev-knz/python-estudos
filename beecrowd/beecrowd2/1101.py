n = int(input())

entrada = input().split()

lista = []
for i in range(len(entrada)):
    lista.append(int(entrada[i]))

m = int(input())

for i in range(n):
    print(lista[i] * m, end=' ')