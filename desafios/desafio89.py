# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente

registro = []

while True:
    n = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))

    registro.append([n, [n1, n2]])

    resposta = str(input('Deseja continuar? [Y/N] '))
    if resposta != 'Y':
        break

print('-='*15)
print('No. NOME          MÉDIA')
print('-'*30)

for i in range(0, len(registro)):
    print(f'{i}  {registro[i][0]}           {(registro[i][1][0]+registro[i][1][1])/2}')
print('-'*30)

while True:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if n == 999:
        break
    else:
        for i in range(0, len(registro)):
            if i == n:
                print(f'Notas de {registro[i][0]} são {registro[i][1]}')
                print('-'*30)