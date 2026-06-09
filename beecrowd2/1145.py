def Le_Matriz(mat, n):
    mat = []
    for i in range(n):
        entrada = input().split()
        linha = []
        for j in range(n):
            linha.append(int(entrada[j]))
        mat.append(linha)

    return mat

def Soma_lin(mat, n):
    matriz = []
    for i in range(n):
        soma = 0
        for j in range(n):
            soma += mat[i][j]
        matriz.append(soma)
    return matriz

def Soma_col(mat, n):
    matriz = []
    for i in range(n):
        soma = 0
        for j in range(n):
            soma += mat[j][i]
        matriz.append(soma)
    return matriz

def Soma_dia(mat, n):
    matriz = []
    soma1, soma2 = 0, 0
    for i in range(n):
        for j in range(n):
            if i == j:
                soma1 += mat[i][j]
    matriz.append(soma1)
    for i in range(n-1, -1, -1):
        for j in range(n, -1, -1):
            if i == j:
                soma2 += mat[i][j]
    matriz.append(soma2)
    return matriz

def Verifica_iguais(lista):
    for i in range(len(lista)):
        if i == 0:
            valor = lista[i]
        else:
            if lista[i] != valor:
                return False
    return valor
        


num = int(input())
matri = []

asd = Le_Matriz(matri, num)
a = Soma_lin(asd, num)
b = Soma_col(asd, num)
c = Soma_dia(asd, num)

if Verifica_iguais(a) and Verifica_iguais(b) and Verifica_iguais(c):
    if a[0] == b[0] == c[0]:
        print(Verifica_iguais(a))
    else:
        print('-1')
else:
    print('-1')




