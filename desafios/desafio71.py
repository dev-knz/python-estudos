# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte qual será ao valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues

# Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

r1 = r10 = r20 = r50 = 0
resto = 0

n = int(input('Insira a quantidade a ser retirado: '))

r50 = n // 50
resto = n % 50

r20 = resto // 20
resto = resto % 20

r10 = resto // 10
resto = resto % 10

r1 = resto 

print(f'Foram retirados:\n{r50} cédulas de R$50\n{r20} cédulas de R$20\n{r10} cédulas de R$%10\n{r1} cédulas de R$1')
