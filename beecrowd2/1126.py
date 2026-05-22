n = int(input())

entrada = input().split()
matriz = []

for i in range(len(entrada)):
    matriz.append(int(entrada[i]))

fator = int(input())
achou = False

for i in range(len(matriz)):
    if fator == matriz[i]:
        achou = True
if achou:
    print('S')
else:
    print('N')