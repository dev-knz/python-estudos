# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

r1 = input()
r2 = input()
r3 = input()

if r1 == 'vertebrado':
    if r2 == 'ave':
        if r3 == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if r3 == 'onivoro':
            print('homem')
        else:
            print('vaca')

else:
    if r2 == 'inseto':
        if r3 == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if r3 == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')