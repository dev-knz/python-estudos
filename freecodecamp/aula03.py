# Listas
items = ['Arroz','Feijão','Macarrão','Alface']

# Adicionar elementos na lista é possível, com o comando append().
items.append('Tomate')

# Remover elementos na lista é possível, com o comando remove()
items.remove(items[4])

# Sort ou Sorted
print(sorted(items))

print(items)

# Dicionários

dog = {'name': 'Jorge', 'age': 6}
dog['color'] = 'Brown'
print(dog)

tse = list()
pessoa = dict()

while True:
    n = str(input('Insira o nome: ')).upper()
    pessoa['nome'] = n

    i = int(input('Insira quantos anos ele tem: '))
    pessoa['idade'] = i

    if i > 17:
        pessoa['voto'] = 'OBRIGATÓRIO'
    else:
        pessoa['voto'] = 'NÃO-OBRIGATÓRIO'
    
    tse.append(pessoa.copy())


    r = str(input('Deseja continuar? [Y] ')).upper()
    if r != 'Y':
        break
    
print(tse)
