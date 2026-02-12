# Variáveis compostas (Tuplas)
# Tupla usa parenteses para concatenação, são imutáveis.

fruta = ('Tomate','Morango','Laranja','Uva')

# Maneira mais simples
for fru in fruta:
    print(fru)

# Maneira complexa
for cont in range(0, len(fruta)):
    print(fruta[cont])
    
# Maneira bem mais complexa e completa
for pos, fru in enumerate(fruta):
    print(f'Eu vou comer {fru} na posição {pos}')

# É possível somar tuplas (juntar)
a = (2, 5, 4)
b = (5, 8, 7, 2)
c = a + b

print(c)