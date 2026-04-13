
quantidade, maior_sequencia = 0, 1
aux = 0
while True:
    num = int(input())

    if num == 0:
        break

    if quantidade == 0:
        anterior = num
        quantidade += 1

    if num > anterior:
        maior_sequencia += 1
        aux = maior_sequencia

    else:
        if maior_sequencia > aux:
            aux = maior_sequencia
            maior_sequencia = 0
    
    anterior = num

if quantidade == 0:
    print(f'Nenhum número foi informado.')

else:
    print(f'Maior sequência crescente: {aux}')
    