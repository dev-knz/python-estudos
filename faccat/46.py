lista1 = ['Py', 'is', 'awes']
lista2 = ['thon', ' ', 'ome']

lista3 = list()

for i in range(len(lista1)):
    print(lista1[i] + lista2[i])
    lista3.append(lista1[i] + lista2[i])

print(lista3)