# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

n = float(input('Qual o valor do salário de fulano '))

if n > 1250:
    salario = n*1.10
    print(f'O salário dele agora é: {salario:.2f}')
else:
    salario = n*1.15
    print(f'O salário dele agora é de: {salario:.2f}')