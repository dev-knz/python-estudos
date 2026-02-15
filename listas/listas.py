# Listas 
# São definidas por colchetes [], são mutáveis para mudar elementos, adicionar, eliminar e modificar posição.

lista = ['Arroz', 'Feijão', 'Carne']

# Método .append() adiciona um elemento na lista, e adiciona com um determinado objeto.

lista.append('Macarrão')
print(lista)

# Método .insert(pos,obj) adiciona um objeto em uma posição desejada, vamos colocar o valor string Peixe na posição 0 da lista:

lista.insert(0, 'Peixe')
print(lista)

# Método para deletar um item da lista sem saber o nome do objeto:
# Método del apaga o elemento
del lista[0] # Nesse caso, apagando o Peixe

# Método .pop() para também apagar o elemento
lista.pop(0)

# Caso saiba o nome do objeto, pode utilizar a função .remove(obj):
lista.remove('Macarrão')

# Para verificar se o elemento está na lista, use dessa forma:
if 'Macarrão' in lista:
    lista.remove('Macarrão')

# É possível declarar listas, veja um exemplo:
valores = list(range(4,11))

# Método .sort() organiza os valores da lista em ordem crescente
# Método .sort(reverse=True) organiza os valores da lista em ordem decrescente

v = []
v.append(5)
v.append(9)
v.append(4)

for c, d in enumerate(v):
    print(f'Na posição {c} encontrei o valor {d}')

for i in v:
    print(f'Achei o valor {i}')

