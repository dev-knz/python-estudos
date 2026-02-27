frase = str(input()).replace(' ','').upper()
digito = vogais = consoantes = others = 0

for letras in frase:
    if letras.isdigit():
        digito += 1
    elif letras.isalpha():
        if letras in 'AEIOU':
            vogais += 1
        else:
            consoantes += 1
    else:
        others += 1


print(f'Nessa frase há {len(frase)} caracteres.')
print(f'Nessa frase há {vogais} vogais.')
print(f'Nessa frase há {consoantes} consoantes.')
print(f'Nessa frase há {digito} digitos.')
print(f'Nessa frase há {others} sinais de pontuação.')
print(f'Nessa frase há {(digito * 100)/ len(frase):.2f}% de números na frase.')