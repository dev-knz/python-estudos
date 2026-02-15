# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

fut = {}
gols = []
total = 0

fut['nome'] = str(input('Nome do Jogador: '))
fut['partidas'] = int(input(f'Quantas partidas {fut["nome"]} jogou? '))

for i in range(0, fut['partidas']):
    gols.append(int(input(f'Quantos gols na partida {i}? '))) 
    total = total + gols[i]
fut['gols'] = gols.copy()
fut['total'] = total

print('=-'*15)
print(f'O campo nome tem o valor {fut["nome"]}')
print(f'O campo gols tem o valor {fut["gols"]}')
print(f'O campo total tem o valor {fut["total"]}')
print('=-'*15)

print(f'O jogador {fut["nome"]} jogou {fut["total"]} partidas')
for i in range(0, fut['partidas']):
    print(f'    Na partida {i} marcou {fut["gols"][i]}')