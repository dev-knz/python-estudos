quantidade, soma, media, par, negativo = 0, 0, 0, 0, 0

while True:
    num = int(input())

    if num == 0:
        break

    if quantidade == 0:
        maior = num
        menor = num
    
    else:
        if num > maior:
            maior = num
        
        if menor > num:
            menor = num
    
    if num % 2 == 0:
        par += 1

    if num < 0:
        negativo += 1

    quantidade += 1
    soma += num
        
    
if quantidade == 0:
    print('Nenhum número foi informado.')
else:
    media = soma / quantidade

    print(f'Quantidade: {quantidade}\nSoma: {soma}\nMedia: {media:.2f}\nMaior: {maior}\nMenor: {menor}\nPares: {par}\nNegativos: {negativo}')