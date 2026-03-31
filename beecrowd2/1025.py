# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

choice, quant = map(int, input().split())

if choice == 1:
    quant = quant * 4
elif choice == 2:
    quant = quant * 4.5
elif choice == 3:
    quant = quant * 5
elif choice == 4:
    quant = quant * 2
else:
    quant = quant * 1.5

print(f'Total: R$ {quant:.2f}')