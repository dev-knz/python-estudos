# Faça um programa que leia as 3 notas de um aluno, e realize a média ponderada respeitando os seguintes pesos respectivos: 2, 3 e 5.


n1 = int(input('Insira a nota do aluno: '))
n2 = int(input('Insira a nota do aluno: '))
n3 = int(input('Insira a nota do aluno: '))

media = ((n1*2) + (n2*3) + (n3*5))/10

print(f'A média ponderada desse aluno é de {media:.2f}')

