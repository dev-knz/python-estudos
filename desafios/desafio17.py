# Faça um programa que leia o cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

import math 

ct1 = int(input('Coloque o valor do cateto adjacente '))
ct2 = int(input('Coloque o valor para o cateto oposto '))

hipo = math.hypot(ct1, ct2)

print(hipo)
print(f'A hipotenusa é de: {hipo}')