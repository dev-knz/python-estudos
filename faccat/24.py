# 1
n = int(input())

if n % 2 == 0:
    print('PAR')

else:
    print('IMPAR')

# 2
soma = 0
while True:
    
    num = int(input())
    if not num: 
        break

    soma += num

# 3

x,y = map(int, input().split())

menor = min(x, y)
maior = max(x, y) 

for i in range(menor, maior+1):
    print(i)
