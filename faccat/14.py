ano_atual = int(input())
ano_nascimento = int(input())

voto = ano_atual - ano_nascimento

if voto >= 18:
    print(f'voto obrigatório')
elif voto >= 16:
    print(f'voto opcional')
else:
    print(f'não pode votar')