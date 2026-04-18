lista = [10, 20, 30, 10, 40, 10, 50]

alvo = int(input())
contagem = 0

for i in lista:
    if i == alvo:
        contagem += 1
print(f'O alvo {alvo} apareceu {contagem} vezes.')
