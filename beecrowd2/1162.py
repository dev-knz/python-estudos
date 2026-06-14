def Le_Matriz(mat, linhas):
    mat = []

    for i in range(linhas):
        entrada = input().split()
        linhas = []

        for j in range(len(entrada)):
            linhas.append(int(entrada[j]))
        mat.append(linhas)
    return mat

def Busca_Maior(mat, linhas):
    maior = mat[0][0]
    for i in range(linhas):
        for j in range(len(mat[i])):
            if mat[i][j] > maior:
                maior = mat[i][j]
    return maior

def Multiplica_mat(mat, linhas, num):
    for i in range(linhas):
        for j in range(len(mat[i])):
            mat[i][j] = mat[i][j] * num
    return mat

def Imprime_matriz(mat, linhas):
    for i in range(linhas):
        for j in range(len(mat[i])):
            print(mat[i][j], end=' ')
        print()

n, m = input().split()

n = int(n)
m = int(m)

lista = []
lista = Le_Matriz(lista, n)

x = Busca_Maior(lista, n)
lista = Multiplica_mat(lista, n, x)
Imprime_matriz(lista, n)
