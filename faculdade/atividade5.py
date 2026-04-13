
quantidade, soma, media, mult = 0, 0, 0, 0

lista = list()
while True:
    num = int(input())

    if num < 0:
        break

    if quantidade == 0:
        maior = num
        menor = num
    
    else:
        if num > maior:
            maior = num
        
        if num < menor:
            menor = num
    
    if num % 3 == 0:
        mult += 1

    soma += num
    quantidade += 1
    lista.append(num)


    
if quantidade == 0:
    print('Nenhum número válido foi informado.')

else:
    media = soma / quantidade

    cont = 0

    for i in lista:
        if i > media:
            cont += 1
    
    print(f'Quantidade: {quantidade}\nSoma: {soma}\nMedia: {media:.2f}\nMaior: {maior}\nMenor: {menor}\nMultiplos de 3: {mult}\nAcima da media: {cont}')