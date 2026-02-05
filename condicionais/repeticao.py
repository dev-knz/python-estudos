# Repetição serve para facilitar a estrutura do programa e algoritmo.
# Estudo de For

# Sintaxe como exemplo

for i in range(1,10):
    print(i)

# Range define o intervalo do for, enquanto a variável i serve justamente para ser um laço condicional. Para terminar um for, basta colocar um 'break'. 

# Você pode colocar a interação na terceira virgula, assim:

for i in range(1,10,2):
    print(i)

# Basicamente ficaria assim: for i in range (comeco, final, intervalo)

# --------------------------------------------------------------------
# Estudo de While - Enquanto
# Quando não sabemos o limite, usamos o while, caso contrário é for.

# Sintaxe como exemplo:

c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')

# Nesse caso, sabemos o limite, então o problema poderia ser resolvido com mais simplicidade com o for.

p = 1
while not p == 0:
    p = int(input('Insira um número '))
print('Fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')
