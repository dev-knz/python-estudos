# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

c = float(input('Insira o valor da casa '))
s = float(input('insira o salário do comprador '))
t = int(input('Insira em quantos anos ele irá pagar '))

p = (c/t)

if p > s/0.7:
    print('O empréstimo foi negado')
else:
    print(f'Empréstimo aprovado, sua parcela é de {p:.2f}')
