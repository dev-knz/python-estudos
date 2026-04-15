
carros_vendidos = int(input())
salario = float(input())
comission = float(input())

s = salario

for i in range(carros_vendidos):
    carro = float(input('Valor do carro: '))

    s = s + (carro * 5/100)

s = s + (comission * carros_vendidos)

print(f'Salário líquido: {salario}\nSalário Bruto: {s}')
