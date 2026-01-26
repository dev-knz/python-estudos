# Escreva um programa que leia um valor em metros e o exiba
# convertido em centimetros e milímetros

n1 = float(input('Digite um valor para metros '))

print('{:.2f} metros'.format(n1))
print('{:.2f} centímetros'.format(n1*100))
print('{:.2f} milímetros'.format(n1*1000))