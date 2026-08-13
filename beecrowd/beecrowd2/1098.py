n, m = input().split()

n = int(n)
m = int(m)

const1 = list()
const2 = list()

entrada = input().split()
for i in range(n):
    const1.append(int(entrada[i]))

entrada = input().split()
for i in range(m):
    const2.append(int(entrada[i]))

resultados = list()
aux = False
for i in range(len(const1)):
    for l in range(len(const2)):
        if const1[i] == const2[l]:
            resultados.append(const1[i])
            aux = True
if aux:
    for i in range(len(resultados)):
        print(resultados[i], end=' ')
else:
    print('N')

