lista = ['Mike', '', 'Emma', 'Kelly', '', 'Brad']

for i in lista:
    if i == '':
        lista.remove('')

print(lista)