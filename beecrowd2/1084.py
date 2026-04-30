binario = input().split()

for i in range(len(binario)):
    binario[i] = int(binario[i])

x = int(input())

inicio, fim = 0, len(binario)
meio = (len(binario) - 1) // 2
achou = False
percorre = 0

while not achou and percorre < len(binario):
    for i in range(inicio, fim):
        if binario[meio] == x:
            achou = True
        if binario[meio] < x:
            inicio = meio
            meio = fim+1 - inicio
        if binario[meio] > x:
            fim = meio
            meio = fim - 1
            inicio = 0
        percorre += 1

fim = len(binario)
if binario[fim-1] == x:
    meio = len(binario) - 1
    achou = True

if achou:
    print(f'O elemento {x} foi encontrado na posição {meio+1}')
else:
    print(f'O elemento {x} não foi encontrado.')
