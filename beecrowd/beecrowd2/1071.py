n = int(input())

linha, aux = 1, 0

while linha != n + 1:
    aux += 1
    
    if aux == 3:
        print(f'{linha**aux}')
        aux = 0
        linha += 1
    else:
        print(f'{linha**aux}', end=' ')