# Definindo o tamanho da lista/for
num = int(input())

lista = list()
for i in range(num):
    aberto, fechado = input().split()
    aberto = int(aberto)
    fechado = int(fechado)

    lista.append(aberto)
    lista.append(fechado)

aberto, fechado = 0, 0
aux, mes = 0, 1
for i in range(1, num*2, 2):
    print(f'Mês {mes}: ', end='')
    print(f'{lista[i]*100/lista[i-1]:.2f}% - ', end='')
    aberto += lista[i-1]
    fechado += lista[i]

    aux = fechado*100/aberto
    print(f'{aux:.2f}%')
    mes += 1