# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o digito 9
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os números pares

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
n4 = int(input('Digite um valor: '))

tpl = (n1, n2, n3, n4)

print(f'Apareceram {tpl.count(9)} vezes')
print(f'O valor 3 apareceu na primeira vez na posição {tpl.index(3)}')
print(f'Os valores pares são: ')

for i in range(0, len(tpl)):
    if tpl[i] % 2 == 0:
        print(tpl[i])
        
