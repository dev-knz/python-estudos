def area_triangulo(base, altura):
    area = base * altura
    return f'{area:.2f}'


base = float(input())
altura = float(input())

print(area_triangulo(base,altura))
