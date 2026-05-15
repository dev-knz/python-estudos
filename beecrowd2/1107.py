n = int(input())

lista = list()
entrada = input().split()

for i in range(n):
    lista.append(int(entrada[i]))

picos = 0
for i in range(2, n-1):
    if lista[i] > lista[i-1] and lista[i] > lista[i+1]:
        picos += 1
print(picos)
    