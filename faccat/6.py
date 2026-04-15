salario = float(input())
reajuste = float(input())

reajuste = reajuste / 100

novo_salario = salario * (reajuste + 1)

print(f'O novo salário do funcionário é de: R$ {novo_salario:.2f}')