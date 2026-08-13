n = int(input())

temperatura = list()
entrada = input().split()

for i in range(n):
    temperatura.append(int(entrada[i]))

m = int(input())
soma = 0
for i in range(n):
    if temperatura[i] < m:
        soma += 1
print(soma)