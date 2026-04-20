lista = [5, 10, 15, 20, 25]

encontrar = int(input())
substituir = int(input())

for i in range(len(lista)):
    if lista[i] == encontrar:
        lista[i] = substituir

print(lista)