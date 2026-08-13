n = int(input())

entrada = input().split()
lista = list()

for i in range(len(entrada)):
    lista.append(int(entrada[i]))

pico = 0
for i in range(2, n-1):
    if lista[i-1] < lista[i] > lista[i+1]:
        pico += 1
print(pico)
