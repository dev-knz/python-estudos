n = int(input())

entrada = input().split()
lista = list()

for i in range(n):
    lista.append(int(entrada[i]))

fator = int(input())

x = 0
for i in range(n):
    if fator == lista[i]:
        x += 1
print(x)