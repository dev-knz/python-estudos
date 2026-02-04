# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: 

# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

n = float(input('Informe o valor do produto: '))

f = input('Digite o que corresponde nos colchetes a forma de pagamento:\n1) [Dinheiro]\n2) [Cartão] à vista\n3) [2x] no cartão\n4) [3x] no cartão\n ')

if f.strip().upper() == 'DINHEIRO':
    print(f'O valor pago será de {n*0.9}')
elif f.strip().upper() == 'CARTÃO':
    print(f'O valor pago será de {n*0.95}')
elif f.strip().upper() == '2X':
    print(f'O valor pago será de {n}')
else: 
    print(f'O valor pago será de {n*1.20}')