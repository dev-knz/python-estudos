def Le_matriz(mat, linhas):
    mat = []

    for i in range(linhas):
        entrada = input().split()
        linha = []
        for j in range(linhas):
            linha.append(int(entrada[j]))
        mat.append(linha)
    return mat

def Busca_maior(mat, linhas):
    maior = mat[0][0]

    for i in range(linhas):
        for j in range(linhas):
            if mat[i][j] > maior:
                maior = mat[i][j]
                x, y = i, j
    
    return maior, x, y

matriz = []
n = int(input())
matriz = Le_matriz(matriz, n)

resposta = Busca_maior(matriz, n)
print(f'O maior elemento da matriz é {resposta[0]} e se encontra na linha {resposta[1] + 1} e coluna {resposta[2] + 1}')