# Listas parte 2

dados = list()
dados.append('Pedro')
dados.append(25)

pessoas = list()
pessoas.append(dados[:]) # Elemento 0 será a lista de dados completa, graças a sintaxe ':'

# Nesse momento estamos aprendendo a colocar listas dentro de listas

print(pessoas)

# Mas é possível definir listas através da concatenação inicial.
# Chamamos de lista composta.

pessoa = [['Pedro', 25], ['Maria', 19], ['João', 32]]

# Verificação:
print(pessoa)

# Dentro das listas, nós temos o indice da lista anterior
# Isso fica mais visível dentro de um exemplo

print(pessoa[0][0]) # Nesse caso, estamos pegando o índice 0 da lista 'pessoa' e também pegando o índice 0 da lista ['Pedro', 25]
print(pessoa[1][1]) # Aqui, estamos pegando o número 19, da lista ['Maria',19]

# Parece difícil, mas é questão de costume.

'''
    Anotações do professor:
'''

teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste) # Nesse momento, criamos uma conexão. Para evitar isso, vamos criar uma cópia
galera.append(teste[:]) # Aqui está correto.

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)

print(galera)

gs = [['João', 29], ['Paulo', 13]]

for p in gs:
    print(p[0])

pessoal = list()
dados = list()
for c in range(0, 3):
    dados.append(str(input('Insira o nome: ')))
    dados.append(int(input('Insira o número: ')))
    pessoal.append(dados[:])
    dados.clear()
    