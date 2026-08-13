n = int(input())

lista = list()
for i in range(n):
    n1, n2, n3 = input().split()

    n1 = int(n1)
    n2 = int(n2)
    n3 = float(n3)

    lista.append(n1)
    lista.append(n2)
    lista.append(n3)

id, km, litros = 0, 1, 2
media = list()

for i in range(n):
    print(f'{lista[id]} {lista[km]/lista[litros]:.2f}')
    media.append(lista[km]/lista[litros])
    id += 3
    km += 3
    litros += 3
print(f'Piores médias:')
media = sorted(media)
print(f'{media[0]:.2f}\n{media[1]:.2f}')