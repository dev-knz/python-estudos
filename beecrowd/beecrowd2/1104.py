n = int(input())

entrada = input().split()

lista = list()
for i in range(len(entrada)):
    lista.append(int(entrada[i]))
    
for i in range(n):
    if i + 3 <= n - 1:
        if i == 0:
            lucro = lista[i] + lista[i+1] + lista[i+2] + lista[i+3]
        else:
            soma = lista[i] + lista[i+1] + lista[i+2] + lista[i+3]
            if soma > lucro:
                lucro = soma
print(lucro)