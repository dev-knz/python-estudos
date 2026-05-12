n = int(input())

entrada = input().split()
lista = list()

for i in range(n):
    lista.append(int(entrada[i]))
fator = int(input())

for i in range(n):
    print(lista[i] * fator, end=' ')