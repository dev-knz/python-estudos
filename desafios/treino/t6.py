# Uma revendedora de carros usados paga a seus funcionários um salário fixo, adicionado a uma comissão fixa por cada carro vendido e mais 5% sobre o total de vendas efetuadas. Escreva um algoritmo que leia o número de carros vendidos, o valor total de vendas, o valor da comissão e o salário fixo.

s = int(input('Insira o salário do funcionário: '))
t = int(input('Insira o valor total das vendas realizadas por dado funcionário: '))
v = int(input('Insira a quantidade de carros vendidos: '))
c = int(input('Insira o valor da comissão recebida pelo funcionário: '))

resultado = s + (t * 5/100) + (v * c)

