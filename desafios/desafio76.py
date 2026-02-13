# Crie um programa que tenha uma tupla única com o nome do produto e preço na sequência. Depois exiba uma listagem dos produtos com os preços em seguida

est = ('Pão', 5, 'Manteiga', 7, 'Salgadinho', 2)

pro = 0
pre = 1

print('LISTA DE PRODUTOS')

while True:
    if(pre > len(est)):
        break
    else:
        print(f'{est[pro]}...R${est[pre]}')
    pro += 2
    pre += 2