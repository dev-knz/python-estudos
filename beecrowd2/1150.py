v = int(input())

matriz = []
contagem = 0

for i in range(3):
    matriz.append(int(input()))
    if v >= matriz[i]:
        v -= matriz[i]
        contagem += 1

print(contagem) 


