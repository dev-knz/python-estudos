n = int(input())

lista = input().split()
media = 0

for i in range(len(lista)):
    lista[i] = int(lista[i])
    media += lista[i]

media = media // n
contagem = 0

for i in range(len(lista)):
    if lista[i] > media:
        contagem += 1
print(contagem)