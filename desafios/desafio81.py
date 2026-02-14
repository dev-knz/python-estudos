# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

resp = 'Y'
lista = []
exs = qntd = 0

while resp == 'Y':
    n = int(input('Digite um valor: '))
    lista.append(n)
    qntd += 1 

    if n == 5:
        exs += 1

    resp = str(input('Deseja continuar? [Y/N] ')).upper()
print(f'Foram digitados {qntd} números.')

lista.sort(reverse=True)
print(f'A lista em ordem decrescente é: {lista}')

print(f'O número 5 foi digitado {exs} vezes')
    