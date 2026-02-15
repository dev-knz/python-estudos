# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

lista = []
linha = []
coluna = []
valor = []
cnt = 1

for i in range(0,3):
    for v in range(0,3):
        n = int(input(f'Digite um valor para [{i}, {v}]: '))

        linha.append(i)
        coluna.append(v)
        valor.append(n)

        lista.append([linha[:], coluna[:], valor[:]])

        linha.clear()
        coluna.clear()
        valor.clear()
    
for p in lista:
    if cnt <= 3:
        print(f'{p[2]} ', end='')
        
    else:
        
        print('\n')
        print(f'{p[2]} ', end='')
        cnt = 1
    cnt += 1
        