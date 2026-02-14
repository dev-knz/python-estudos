# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados em ordem crescente.

lista = []
resp = 'Y'
i = exs = 0

while resp == 'Y':
    n = int(input('Digite um valor: '))

    for i in range(0, len(lista)):
        if n == lista[i]:
            print(n)
            print('Esse valor já existe na lista, tente novamente.')
            exs = 1
    if exs == 0:
        lista.append(n)
        print('Valor adicionado com sucesso.')
    i = exs = 0
    resp = str(input('Deseja continuar? [Y/N] '))

    if resp == 'N':
        break

lista.sort()
print(f'A lista é: {lista}')
    