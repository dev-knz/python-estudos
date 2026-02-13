# Ler 3 valores e escrever em ordem crescente

n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
n3 = int(input('Insira o terceiro valor: '))

if n1 > n2 > n3:
    print(f'{n3}, {n2} e {n1}')
elif n1 > n3 > n2:
    print(f'{n2}, {n3} e {n1}')
elif n2 > n1 > n3:
    print(f'{n3}, {n1} e {n2}')
elif n2 > n3 > n1:
    print(f'{n1}, {n3} e {n2}')
elif n3 > n2 > n1:
    print(f'{n1}, {n2} e {n3}')
else: 
    print(f'{n2}, {n1} e {n3}')