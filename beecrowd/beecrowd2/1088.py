num = int(input())

lista = input().split()

for i in range(len(lista)):
    lista[i] = int(lista[i])

x = int(input())
contagem = 0

for i in range(len(lista)):
    if x == lista[i]:
        contagem += 1
print(contagem)