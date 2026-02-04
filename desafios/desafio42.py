# Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

n1 = int(input('Insira o primeiro valor '))
n2 = int(input('Insira o segundo valor '))
n3 = int(input('Insira o terceiro valor '))

if (n1 + n2 > n3) and (n1 + n3 > n2) and (n3 + n2 > n1):
    if n1 == n2 and n1 == n3:
        print('Este triângulo é Equilátero')
    if n1 == n2 != n3 or n1 == n3 != n2 or n2 == n3 != n1:
        print('Este triângulo é Isósceles')
    if n1 != n2 != n3:
        print('Este triângulo é escaleno')
else: 
    print('Ele não pode ser um triângulo.')