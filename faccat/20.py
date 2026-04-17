n = int(input())
ult, inverso = 0, 0
aux = n
while aux != 0:
    ult = aux % 10
    aux = aux // 10
    inverso = inverso * 10 + ult
if inverso == n:
    print('Sim')
else:
    print('Não')