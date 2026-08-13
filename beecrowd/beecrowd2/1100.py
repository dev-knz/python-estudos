n = int(input())

minado = list()

for i in range(n):
    minado.append(int(input()))

mina = list()
for i in range(n):
    if i == 0:
        mina.append(minado[i] + minado[i+1]) 
    elif i == (n-1):
        mina.append(minado[i] + minado[i-1])
    else:
        mina.append(minado[i-1] + minado[i] + minado[i+1])

for i in range(len(mina)):
    print(mina[i])
        

