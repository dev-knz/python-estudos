# Ler 3 valores e exiba o maior

n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
n3 = int(input('Insira o terceiro valor: '))

if n1 > n2 > n3 or n1 > n3 > n2:
    print(f'O valor {n1} é o maior')
elif n2 > n1 > n3 or n2 > n3 > n1:
    print(f'O valor {n2} é o maior')
elif n3 > n1 > n2 or n3 > n2 > n1:
    print(f'O valor {n3} é o maior')