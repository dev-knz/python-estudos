# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7.0 por cada Km acima do limite.

n = int(input('Insira a sua velocidade '))

if n > 80:
    multa = (n - 80)*7
    print(f'O valor que deverá ser pago na multa, será de: R${multa}.0')
else:
    print('O carro está dentro da velocidade permitida! ')