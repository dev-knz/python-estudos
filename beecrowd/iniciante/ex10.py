# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

c1, n1, v1 = input().split()
c2, n2, v2 = input().split()

n1 = int(n1)
v1 = float(v1)
n2 = int(n2)
v2 = float(v2)

total = (n1 * v1) + (n2 * v2)

print(f'VALOR A PAGAR: R$ {total:.2f}')