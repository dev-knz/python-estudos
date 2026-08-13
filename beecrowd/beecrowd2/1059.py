# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
continuar = True
media, contador = 0, 0

while continuar == True:
    n = float(input())

    if n >= 0 and n <= 10:
        media += n
        contador += 1
    
    else:
        print('nota invalida')

    if contador == 2:
        media = media / 2
        print(f'media = {media:.2f}')

        media = 0
        contador = 0
        
        while True:
            print('novo calculo (1-sim 2-nao)')
            resposta = int(input())

            if resposta == 1:
                continuar = True
                break

            if resposta == 2:
                continuar = False
                break
        
    
        