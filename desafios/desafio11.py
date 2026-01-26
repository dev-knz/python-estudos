# Faça um programa que leia a largura e a altura de uma parede em metros
# Calcule a sua área e a quantidade de tinta necessário para pintá-la, sabendo que
# cada litro de tinta pinta uma área de 2m²

a1 = float(input('Escolha o primeiro valor '))
a2 = float(input('Escolha o segundo valor '))

area = a1 * a2
tinta = area/2

print(f'A área desta parede é de: {area}')
print(f'A quantidade de litros de tinta usada é de: {tinta}')