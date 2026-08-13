def Le_matriz(mat, linhas):
    mat = []

    for i in range(linhas):
        entrada = input().split()
        linha = []
        for j in range(len(entrada)):
            linha.append(int(entrada[j]))
        mat.append(linha)

    return mat

def Verifica_Linhas(mat, linhas):
    lista = []

    for i in range(1, linhas + 1):
        lista.append(i)
    
    latino = True
    for i in range(linhas):
        aux = lista.copy()
        for j in range(linhas):
            if mat[i][j] in aux:
                aux.remove(mat[i][j])
            else:
                latino = False
    return latino

def Verifica_Colunas(mat, linhas):
    lista = []

    for i in range(1, linhas+1):
        lista.append(i)

    latino = True
    for i in range(linhas):
        aux = lista.copy()
        for j in range(linhas):
            if mat[j][i] in aux:
                aux.remove(mat[i][j])
            else:
                latino = False
    return latino

n = int(input())
mat = []

matriz = Le_matriz(mat, n)
a = Verifica_Colunas(matriz, n)
b = Verifica_Linhas(matriz, n)

if a and b:
    print('L')
else:
    print('N')