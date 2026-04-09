n = int(input())

numero, aux = 0, n
n = str(n)
for i in range(len(n)):

    ult = aux % 10
    aux = aux // 10

    numero = numero + ((2**i) * ult)
print(numero)