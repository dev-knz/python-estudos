# Condição: If e Else
# Não existem condições bipolares, que funcionam aos dois métodos ao mesmo tempo.

n = int(input('Insira um número '))

if n > 10:
    print('Seu número está válido ')
else:
    print('Seu número não é válido ')
print('Fim')

# Método simplificado
tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo'if tempo<=3 else 'carro velho')

# Sinceramente, não é muito recomendado para iniciantes como eu.
# Mais exemplos abaixo

nome = input('Qual seu nome? ')
if nome == 'Kevin':
    print('A gente tem o mesmo nome')
else:
    print('Nome bacana! ')