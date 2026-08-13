n = int(input())

entrada = input().split()
lista = list()

for i in range(n):
    lista.append(int(entrada[i]))

preju, soma = 0, 0
for i in range(n):
    if i + 3 <= n-1:
        if i == 0:
            preju = lista[i] + lista[i+1] + lista[i+2] + lista[i+3]
        else:   
            soma = lista[i] + lista[i+1] + lista[i+2] + lista[i+3]
            if preju < soma:
                preju = soma 
print(preju)
