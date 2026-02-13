# Leia duas notas e exiba a média aritmética.

n1 = int(input('Insira a primeira nota: '))
n2 = int(input('Insira a segunda nota: '))

media = (n1+n2)/2

if media > 5.9:
    print(f'O aluno foi aprovado.')
else: 
    print(f'O aluno foi reprovado.')