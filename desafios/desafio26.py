# Faça um programa que leia uma frase pelo teclado e mostre:

# Quantas vezes aparece a letra 'a'.
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

n = input('Insira uma frase ')

print(n.upper().count('A'))
print(n.upper().find('A'))
print(n.upper().rfind('A'))