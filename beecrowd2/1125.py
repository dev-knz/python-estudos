entrada = input().split()

matriz = []
for i in range(len(entrada)):
    matriz.append(int(entrada[i]))

diferenca = []

for i in range(len(matriz)):
    if i + 1 < len(matriz):
        diferenca.append(abs(matriz[i] - matriz[i+1]))

trocou = True
while trocou:
    trocou = False
    for i in range(len(diferenca) - 1):
        if diferenca[i] > diferenca[i+1]:
            diferenca[i], diferenca[i + 1] = diferenca[i + 1], diferenca[i]
            trocou = True

resposta = True
for i in range(len(diferenca)):
    for j in range(len(diferenca)):
        if i < len(diferenca) and j < len(diferenca):
            if diferenca[i] == diferenca[j] and j != i:
                resposta = False
if not resposta:
    print('N')

else:
    print('C')