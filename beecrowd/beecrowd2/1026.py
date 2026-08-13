# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
n1, n2, n3, n4 = map(float, input().split())

media = (n1 * 2) + (n2 * 3) + (n3 * 4) + n4
media = media / 10
print(f'Media: {media:.1f}')
if media >= 7:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    exame = float(input())
    
    print(f'Nota do exame: {exame:.1f}')
    media = media + exame 
    media = media / 2

    if media >= 5:
        print('Aluno aprovado.')

    else:
        print('Aluno reprovado.')
    
    print(f'Media final: {media:.1f}')