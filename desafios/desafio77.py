# Crie um programa que tenha uma tupla com várias palavras. Depois disso, você deve mostrar as vogais de cada palavra.

tpl = ('APRENDER', 'PROGRAMAR', 'LER', 'JOGAR', 'ROBLOX')

for palavra in tpl:
    print(f'\nNa palavra {palavra} temos: ', end='')
    for letra in palavra:
        if letra in 'AEIOU':
            print(letra, end=' ')
