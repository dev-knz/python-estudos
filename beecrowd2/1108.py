n = int(input())

entrada = input().split()
lista = []

for i in range(len(entrada)):
    lista.append(int(entrada[i]))

for i in range(n):
    if i == 0:
        menor = lista[i]
    else:
        if lista[i] < menor:
            menor = lista[i]
print(menor)