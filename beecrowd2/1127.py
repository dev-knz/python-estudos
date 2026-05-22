n = int(input())

entrada = input().split()
matriz = []
media = 0

for i in range(len(entrada)):
    matriz.append(int(entrada[i]))
    media = media + matriz[i]
media = media / n

contador = 0
for i in range(len(matriz)):
    if matriz[i] < media:
        contador += 1
print(contador)
