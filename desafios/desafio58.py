# Melhore o jogo do Desafio 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

n1 = random.randint(0,10)
tentativas = 0

n = int(input('Insira o valor: '))

while n != n1:
    tentativas += 1
    n = int(input('Insira o valor: '))
print(f'Você acertou em {tentativas} tentativas ')


