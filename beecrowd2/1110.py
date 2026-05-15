n = int(input())

lista = list()
entrada = input().split()

for i in range(n):
    lista.append(int(entrada[i]))
    
certo = True
for i in range(n):
    if i == 0:
        degrau = lista[i]
    else:
        if degrau < lista[i]:
            degrau = lista[i]
        else:
            certo = False
if certo:
    print('Sim')
else:
    print('Não')