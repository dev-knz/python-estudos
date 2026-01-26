# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
import math
from math import trunc

n = float(input('Digite um número '))

print(f'A parte inteira do seu número é {math.trunc(n)}')