industria = float(input())

distribuidor = 0.28
imposto = 0.45

valor = industria + (industria * distribuidor) + (industria * imposto)

print(f'Preço do carro: {valor:.2f}')