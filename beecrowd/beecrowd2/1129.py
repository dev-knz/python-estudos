n = int(input())

matriz = []

for i in range(n):
    entrada = input().split()
    linha = []
    for i in range(n):
        linha.append(int(entrada[i]))
    matriz.append(linha)

entrada = input().split()

cidades = []

for i in range(len(entrada)):
    cidades.append(int(entrada[i]))

primeiro, segundo = cidades[0] - 1, cidades[1]
i = 0

soma = 0

while i + 1 < len(cidades):
    soma = soma + matriz[cidades[i] - 1][cidades[i + 1] - 1]
    i += 1
print(soma)
    
    
