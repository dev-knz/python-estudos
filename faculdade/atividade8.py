n = int(input())

inverso = 0 # Definindo uma variável para armazenar o inverso do número principal
n2 = n # Copiando a variável principal


while n2 != 0:
    ult = n2 % 10

    inverso = inverso * 10 + ult
    n2 = n2 // 10

if inverso == n:
    print('S')
else:
    print('N')