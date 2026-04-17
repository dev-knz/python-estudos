number = [100, 50, 400, 500]

# Alterando o elemento
number[1] = 200
print(f'Atualizado (Alteração): {number}')

# Adicionando elemento
number.append(600)
print(f'Atualizado (Anexar): {number}')

# Inserindo elemento
number.insert(2, 300)
print(f'Atualizado (Inserir): {number}')

# Removendo o elemento que possui valor 600
number.pop()
print(f'Atualizado (Remover 600): {number}')

# Remover o elemento de índice 0
number.pop(0)
print(f'Atualizado (Remover Índice 0): {number}')
