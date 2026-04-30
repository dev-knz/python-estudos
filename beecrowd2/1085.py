n1, n2 = input().split()

lista1, lista2 = list(), list()

entrada = input().split()
for i in range(len(entrada)):
    lista1.append(int(entrada[i]))

entrada = input().split()
for i in range(len(entrada)):
    lista2.append(int(entrada[i]))

lista3 = list()
for i in range(len(lista1)):
    for l in range(len(lista2)):
        if lista1[i] == lista2[l]:
            lista3.append(lista1[i])

if lista3:
    for i in range(len(lista3)):
        print(f'{lista3[i]} ', end='')
else:
    print(f'Não há caçadores aptos.')