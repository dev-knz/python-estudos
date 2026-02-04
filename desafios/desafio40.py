# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final sobre a média final.

n1 = float(input('Insira a sua primeira nota '))
n2 = float(input('Insira a sua segunda nota '))

media = (n1+n2)/2

if media > 5.9:
    print(f'Sua média foi {media}, você foi aprovado.')
else:
    print(f'Sua média foi {media}, você reprovou.')