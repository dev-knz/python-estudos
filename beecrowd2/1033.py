# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

h_ini, m_ini, h_fin, m_fin = map(int, input().split())

inicio = h_ini * 60 + m_ini
fim = h_fin * 60 + m_fin

if fim <= inicio:
    fim += 24 * 60

duracao = fim - inicio
hora = duracao // 60
minuto = duracao % 60


print(f'O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)')
