def Le_Matriz(mat, linhas):
    mat = []
    
    for i in range(linhas):
        entrada = input().split()
        linha = []

        for j in range(len(entrada)):
            linha.append(int(entrada[j]))
        mat.append(linha)
    return mat

def Calcula_Sela(mat, linhas, colunas):
    menor = mat[0][0]
    maior = 0
    x, y = 0, 0

    achou_menor, achou_maior = False, True

    for i in range(linhas):
        for j in range(colunas):
            if mat[i][j] < menor:
                x, y = i, j
                achou_menor = True
        if achou_menor:
            for k in range(linhas):
                if not mat[x][y] > mat[k][y] and x != k:
                    achou_maior = False
            if not achou_maior:
                achou_maior = True
            else:
                break
    return mat[x][y], x, y

n, m = input().split()

n = int(n)
m = int(m)

mat = []
mat = Le_Matriz(mat, n)
resultado = Calcula_Sela(mat, n, m)
print(resultado[0], resultado[1], resultado[2])
                

