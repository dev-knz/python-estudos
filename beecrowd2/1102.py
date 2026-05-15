n = int(input())

entrada = input().split()

media = 0
lista = []

for i in range(len(entrada)):   
    lista.append(int(entrada[i]))
    media = media + int(entrada[i])
media = media / n

maior = 0
for i in range(n):
    if lista[i] > media:
        maior += 1
print(maior)