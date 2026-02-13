# Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

number = int(input())
qntd = int(input())
recebe = float(input())

SALARY = qntd * recebe

print(f'NUMBER = {number}')
print(f'SALARY = U$ {SALARY:.2f}')

