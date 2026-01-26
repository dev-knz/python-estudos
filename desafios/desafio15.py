# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
# e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Quantos km's foram percorridos "))
dias = int(input("Quantos dias foram usados com o carro alugado "))

km = km * 0.15
dias = dias * 60

print(f'O valor gasto total para o veículo alugado foi de: {km+dias}')
