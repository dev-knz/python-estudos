n1, n2 = map(int, input().split())

media = (n1 + n2 ) / 2

if media >= 6:
    print(f'Aluno aprovado')
else:
    print(f'Aluno reprovado')
