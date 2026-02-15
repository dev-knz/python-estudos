# Aprimore o desafio anterior, mostrando no final:

# A) A soma de todos os valores pares digitados
# B) A soma dos valores da terceira coluna
# C) O maior valor da segunda linha


lista = []
linha = []
coluna = []
valor = []
cnt = 1
somaA = somaB = maior = 0

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

        if n % 2 == 0:
            somaA = somaA + n

        if i == 1:
            if n > maior:
                maior = n

        if v == 2:
            somaB = somaB + n
    
for p in lista:
    if cnt <= 3:
        print(f'{p[2]} ', end='')
        
    else:
        
        print('\n')
        print(f'{p[2]} ', end='')
        cnt = 1
    cnt += 1

print(f'\nA soma de todos os valores é {somaA}')
print(f'A soma dos valores da terceira coluna é {somaB}')
print(f'O maior valor da linha dois é {maior}')
        