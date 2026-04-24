entrada = input().split()

lista1 = list()
for i in range(len(entrada)):
    lista1.append(int(entrada[i]))

entrada = input().split()

lista2 = list()
for i in range(len(entrada)):
    lista2.append(int(entrada[i]))

i, j = 0, 0
lista3 = list()
while i < len(lista1) and j < len(lista2):
    if lista1[i] < lista2[j]:
        lista3.append(lista1[i])
        i += 1
    else:
        lista3.append(lista2[j])
        j += 1

while i < len(lista1):
    lista3.append(lista1[i])
    i += 1

while j < len(lista2):
    lista3.append(lista2[j])
    j += 1

print(lista3)