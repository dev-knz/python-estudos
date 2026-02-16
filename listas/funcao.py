# Função serve para facilitar e 'automatizar' serviços ou rotinas
# Para concatenar uma função na sintaxe, basta usar 'def'

def mostraLinha():
    print('-'*30)

mostraLinha()
print('SISTEMA DE ALUNOS')
mostraLinha()

# Simplificando

def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)

# Agora a função precisa de um parâmetro
mensagem('Sistema de Alunos')
mensagem('Sistema de Professores')

def somar(a,b):
    print(a+b)

somar(10, 9)
somar(a=134, b=34)
somar(b = 10, a = 1)

# Contador

def contador(*num):
    print(num)


contador(2, 1, 7)
contador(3, 6, 1, 23)
contador(4, 4, 4, 4, 4)


def dobra(lista):
    for i in range(0, len(lista)):
        lista[i] *= 2


lista = [4,3,5,6,7]

dobra(lista)
print(lista)
