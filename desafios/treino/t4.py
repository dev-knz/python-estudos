# Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcule e escreva o percentual que cada um representa em relação aos eleitores.

e = int(input('Insira quantos eleitores existem em um dado município: '))

b = int(input('Insira quantos votos brancos foram feitos: '))
n = int(input('Insira quantos votos nulos foram feitos: '))
v = int(input('Insira quantos votos válidos foram feitos: '))

if b+n+v > e:
    print(f'Parece que há algo de errado, dados demais foram inseridos para a demanda de eleitores da cidade.')
else:
    print(f'{(b/e)*100}% de pessoas votaram em branco.')
    print(f'{(n/e)*100}% de pessoas votaram em nulo.')
    print(f'{(v/e)*100}% de pessoas votaram em alguém.')