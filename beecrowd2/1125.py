n = int(input())

entrada = input().split()
matriz = []

for i in range(len(entrada)):
    matriz.append(int(entrada[i]))
    
fator = float(input())

for i in range(len(matriz)):
    matriz[i] = matriz[i] * fator
    print(f'{matriz[i]:.1f}', end=' ')