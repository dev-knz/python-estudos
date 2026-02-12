# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do brasileirão, na ordem da colocação. Depois mostre:

# Apenas os 5 primeiros colocados
# Os últimos 4 colocados da tabela
# Uma lista em ordem alfabética
# Em que posição está o São Paulo

tabela = ('São Paulo', 'Bahia', 'Bragantino', 'Chapecoense', 'Mirassol', 'Palmeiras', 'Fluminense', 'Coritiba', 'Flamengo', 'Botafogo', 'Athletico-PR', 'Grêmio', 'Vitória', 'Atlético-MG', 'Remo', 'Internacional', 'Santos', 'Vasco', 'Cruzeiro', 'Corinthians')

print(f'Os primeiros cinco colocados são: {tabela[:5]}')
print(f'Os últimos 4 colocados na tabela são: {tabela[-4:0]}')
print(f'Uma lista em ordem alfabética: {sorted(tabela)}')
print(f'Em que posição está o São Paulo: {tabela.index('São Paulo')}')