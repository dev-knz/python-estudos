# Crie um script Python que leia dois números e tente
# mostrar a soma entre elas

n1 = int(input('Escolha o primeiro número: '))
n2 = int(input('Escolha o segundo número: '))
s = n1 + n2

# Maneira um pouco poluído 
print('A soma de' ,n1, '+' ,n2, 'é igual a ' ,s)

# Maneira mais prática e sugestiva 
print('A soma entre {} e {} vale {}'.format(n1, n2, s))

# Exibe a soma dos valores usando o .format
print('A soma desses valores é {}'.format(s))
