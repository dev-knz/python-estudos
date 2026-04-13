total, quantidade, vista, prazo, lista = 0, 0, 0, 0, list() 

while True:
    valor = int(input())
    if not valor:
        break
    num = int(input())
    if not num:
        break
    
    if num == 1:
        vista += valor

    if num == 2:
        prazo += valor
    
    if quantidade == 0:
        maior = valor
        menor = valor
    
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

    quantidade += 1
    total += valor
    lista.append(valor)

if quantidade == 0:
    print('Nenhuma compra foi realizada')
else:
    media = total / quantidade

    cont = 0
    for i in lista:
        if i > media:
            cont += 1 
    
    print(f'Total: {total}\nQuantidade: {quantidade}\nMedia: {media:.2f}\nMaior: {maior}\nMenor: {menor}\nA vista: {vista}\nA prazo: {prazo}\nAcima da media: {cont}')
