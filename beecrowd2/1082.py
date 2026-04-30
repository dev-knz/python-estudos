# Lendo a primeira nota 
n1 = float(input('Insira a primeira nota: '))
# Lendo a segunda nota
n2 = float(input('Insira a segunda nota: '))

# Calculando a média
media = (n1 + n2) / 2
# Frequência
frequencia = int(input('Insira a frequência em porcentagem: '))

# Verifica se o aluno possui a média e frequência necessária para ser aprovado
if media >= 7 and frequencia >= 75:
    print(f'Este aluno foi aprovado, com média: {media:.2f} e presença: {frequencia}%')
# Verifica se o aluno possui a média para a recuperação e frequência necessária 
elif 5.0 <= media <= 7.0 and frequencia >= 75:
    print(f'Este aluno está de recuperação, com média: {media:.2f} e presença: {frequencia}%')
# Caso nenhuma dessas condições sejam verdadeiras, então o aluno reprovou!
else:
    print(f'Este aluno foi reprovado, com média: {media:.2f} e presença: {frequencia}%')
