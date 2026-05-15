n = int(input())

lista = list()
entrada = input().split()
media = 0

for i in range(len(entrada)):
    lista.append(float(entrada[i]))
    media = media + lista[i]
media = media / n

menor, maior = [], []
for i in range(n):
    if lista[i] > media:
        maior.append(lista[i])
    else:
        menor.append(lista[i])

for i in range(len(menor)):
    print(menor[i], end=' ')
print('\n')
for i in range(len(maior)):
    print(maior[i], end=' ')    