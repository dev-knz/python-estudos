# Escreva um algoritmo para ler o salário de um funcionário e em seguida, leia o reajuste do salário do mesmo. Exiba no final do código o novo salário

s = float(input('Insira o salário do funcionário: '))

r = float(input('Insira o reajuste em porcetagem do salário: '))

print(f'O novo salário do funcionário será de: R${s*(1+(r/100))}')