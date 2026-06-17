def Le_Matriz(mat, linhas):
    mat = []
    
    for i in range(linhas):
        entrada = input().split()
        linha = []

        for j in range(len(entrada)):
            linha.append(int(entrada[j]))
        mat.append(linha)
    return mat

def Calcula(mat, linhas, colunas):

    for i in range(linhas):
        menor = mat[i][0]
        x = i
        y = 0

        for j in range(colunas):
            if menor > mat[i][j]:
                menor = mat[i][j]
                x, y = i, j

        eh_maior = True

        for k in range(linhas):
            if not mat[x][y] > mat[k][y] and x != k:
                eh_maior = False

        if eh_maior:
            return mat[x][y], x, y
    return mat[x][y], -1, -1
          
n, m = input().split()

n = int(n)
m = int(m)

mat = []
mat = Le_Matriz(mat, n)
resultado = Calcula(mat, n, m)
if resultado[1] != -1 and resultado[2] != -1:
    print(resultado[0], resultado[1], resultado[2])
else:
    print('Não há ponto de sela')
                

