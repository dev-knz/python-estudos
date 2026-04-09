# Entrada para o for
n = int(input())

# Alcool precisa ser até 70% da gasolina
justo = False

for i in range(n):
    estado, alcool, gasolina = input().split()

    estado = str(estado)
    alcool = float(alcool)
    gasolina = float(gasolina)

    if alcool <= (gasolina * 0.7):
        print(f'{estado}')
        justo = True

if not justo:
    print('*')