# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador

jogador = []
fut = {}
gols = []
total = 0

while True:

    fut['nome'] = str(input('Nome do Jogador: '))
    fut['partidas'] = int(input(f'Quantas partidas {fut["nome"]} jogou? '))

    for i in range(0, fut['partidas']):
        gols.append(int(input(f'Quantos gols na partida {i}? '))) 
        total = total + gols[i]
    fut['gols'] = gols.copy()
    fut['total'] = total
    jogador.append(fut.copy())
    fut.clear()
    gols.clear()

    resposta = str(input('Deseja continuar? [Y/N] '))
    if resposta != 'Y':
        break

print('=-'*15)
print('cod  nome                gols            total')
print('-'*30)
for c,v in enumerate(jogador):
    print(f' {c}   {v["nome"]}               {v["gols"]}            ', end='')
    print(f'{v["total"]}')
print('-'*30)

while True:
    n = int(input('Mostrar dados de qual jogador? '))
    
    if n == 999:
        break
    else:
        print(f'LEVANTAMENTO DO JOGADOR {jogador[n]["nome"]}')
        for i in range(0, jogador[n]['partidas']):
            print(f'    Na partida {i} marcou {jogador[n]["gols"][i]}')
    print('-'*30)
