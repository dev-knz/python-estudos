# Os módulos, também conhecidos como bibliotecas, possuem tecnologias e funcionalidades diversas 
# para facilitar a programação

# Para importar, basta usar a sintaxe: 
import math 
import random

# Para importar somente um item de alguma biblioteca, basta executar este comando
from math import sqrt

num = int(input('Digite um número '))
raiz = math.sqrt(num)

print(f'A raiz quadrada de {num} é {math.ceil(raiz)}')

number = random.randint(1,100)
print(number)

