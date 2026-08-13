n = int(input())

lista = list()
for i in range(n):
    num = int(input())
    lista.append(num)

inicio, fim = 0, len(lista) - 1

while inicio < fim:
    lista[inicio], lista[fim] = lista[fim], lista[inicio]
    inicio += 1
    fim -= 1

for i in range(len(lista)):
    print(f'{lista[i]}', end=' ')