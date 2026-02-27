# Sets
# Mais usado na parte de dados.

set1 = {'Pablo', 'Kevin', 'Pedro'}
set2 = {'Pablo'}

mod = set1 | set2 # Somar sets, porém não coloca elementos repitidos
intersect = set1 & set2 # Pega a intersecção dos elementos

print(mod)
print(intersect)

# Functions

def hello(name = 'my friend'):
    print('Hello ' + name)

hello()

def hello1(name, idade):
    '''
    Docstring for hello1
    
    :param name: nome da pessoa
    :param idade: integer 
    '''

    print(f'Hello {name}, you are {idade} years old!')

hello1('Pablo', 10)
