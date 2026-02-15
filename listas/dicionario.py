# Dicionários servem para personalizar indices para algo mais literal.

# Tupla ()
# Lista []
# Dicionário {}

# Sintaxe de concatenação
dados = dict()
dados = {'nome': 'Pedro', 'idade': 25} 

print(dados['nome'])
print(dados['idade'])

# Para dicionário, o append não funciona, nesse caso o python cria automaticamente
dados['sexo'] = 'M'

# Apaga o indice 'idade'
del dados['idade']

filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
}

print(filme.values()) # Retorna todos os valores do dicionário
print(filme.keys()) # Retorna as chaves, ou seja, os indices do dicionário
print(filme.items()) # Retorna tanto chaves quanto valores

for k, v in filme.items():
    print(f'O {k} é {v}')

locadora = []
locadora.append(filme.copy())

print(locadora[0]['titulo'])

estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil = []
brasil.append(estado1.copy())
brasil.append(estado2.copy())

print(brasil[0]['uf'])