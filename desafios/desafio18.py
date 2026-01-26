# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angle = int(input('Insira um valor de um ângulo: '))

rad = math.radians(angle)

print(f'O cosseno deste valor é {math.cos(angle)}')
print(f'O seno deste valor é {math.sin(angle)}')
print(f'A tangente deste valor é {math.tan(angle)}')