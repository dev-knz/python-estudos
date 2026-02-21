# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.

from desafio107_moeda import metade, dobro, diminuir, aumentar, moeda

p = float(input('Digite o preço: '))
print(f'A metade de {moeda(p)} é de: {moeda(metade(p))}')
print(f'O dobro de {moeda(p)} é de: {moeda(dobro(p))}')
print(f'O valor aumentado de {moeda(p)} é: {moeda(aumentar(p, 20))}')
print(f'O valor diminuido de {moeda(p)} é: {moeda(diminuir(p , 20))}')
