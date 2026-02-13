# Faça um programa que leia o número da conta, saldo da conta, valor debitado e valor creditado do saldo. Veja se ele tem o saldo positivo ou negativo no final das contas

n = int(input('Insira o número da conta: '))
s = float(input('Insira o saldo da conta: '))
d = float(input('Insira o valor debitado da conta: '))
c = float(input('Insira o valor creditado da conta: '))

if d - (s + c) > 0:
    print(f'A conta {n} possui saldo negativo de {(d-c)-s}') 
else:
    print(f'A conta {n} possui saldo positivo de {(d - c) - s}')