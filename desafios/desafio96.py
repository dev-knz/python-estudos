# Faça um programa que tenha uma função chamada area(), que recebe as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area():
    c = int(input('Insira a largura em metros: '))
    l = int(input('Insira o comprimento em metros: '))
    print(f'A área do terreno é de: {c*l}m²')

area()