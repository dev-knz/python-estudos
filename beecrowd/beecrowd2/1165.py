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
    for i in range(linhas):
    
        for j in range(colunas):
            if mat[i][j] < menor:
                menor = mat[i][j]

    maior = [0][0] 
    for i in range(colunas):

        for j in range(linhas):
            if mat[j][i] > maior:
                maior = mat[j][i]
    
    x, y = -1, -1

    for i in range(linhas):
        for j in range(colunas):
            if menor == mat[i][j] and maior == mat[i][j]:
                x, y = i, j

    return maior, x, y

n, m = input().split()

n = int(n)
m = int(m)

mat = []
mat = Le_Matriz(mat, n) 
resposta = Calcula_Sela(mat, n, m)

if resposta[1] == -1 and resposta[2] == -1:
    print('Não há ponto de sela')
else:
    print(resposta[0], resposta[1], resposta[2])
