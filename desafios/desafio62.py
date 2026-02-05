# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

p = int(input('Insira o primeiro termo da operação: '))
r = int(input('Insira a razão da PA: '))

while p < r*10+1:
    print(p)
    p = p+r

n = int(input('Você quer mostrar mais quantos termos? '))
while n != 0 and p < ((r*10+1)+(n*r)):
    print(p)
    p = p+r
print('Fim')
