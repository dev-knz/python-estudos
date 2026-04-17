n = int(input())

sequencia = False

for i in range(n):
    num = int(input())

    if i == 0:
        anterior = num
    
    elif num == anterior:
        sequencia = True
    
    anterior = num

if sequencia:
    print(f'Sim')
else:
    print(f'Nao')